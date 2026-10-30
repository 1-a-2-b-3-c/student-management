import json
import re
import logging
import boto3
from decimal import Decimal
from datetime import datetime, timezone
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

table = boto3.resource('dynamodb').Table('Students')
HEADERS = {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}
FIELDS = ('full_name', 'major', 'email', 'birth_day', 'gpa', 'is_active')
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')


def respond(status, payload):
    return {'statusCode': status, 'headers': HEADERS, 'body': json.dumps(payload, ensure_ascii=False)}


def validate(data):
    unknown = set(data) - set(FIELDS) - {'student_id'}
    if unknown:
        return 'Trường không hợp lệ: ' + ', '.join(sorted(unknown))
    for f in ('full_name', 'major'):
        if f in data and not data[f].strip():
            return f'{f} không được để trống.'
    if data.get('email') and not EMAIL_RE.match(data['email']):
        return 'email không đúng định dạng.'
    if data.get('birth_day'):
        try:
            datetime.strptime(data['birth_day'], '%Y-%m-%d')
        except ValueError:
            return 'birth_day phải có dạng YYYY-MM-DD.'
    if 'gpa' in data:
        g = data['gpa']
        if not isinstance(g, (int, Decimal)) or not 0 <= g <= 4:
            return 'gpa phải là số từ 0 đến 4.'
    return None


def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body') or '', parse_float=Decimal)

        student_id = body.get('student_id')
        if not isinstance(student_id, str) or not student_id.strip():
            return respond(400, {'error': 'Thiếu tham số student_id bắt buộc.'})

        error = validate(body)
        if error:
            return respond(400, {'error': error})

        fields = {k: (body[k].strip() if isinstance(body[k], str) else body[k]) for k in FIELDS if k in body}
        if not fields:
            return respond(400, {'error': 'Không có trường nào để cập nhật.'})
        fields['updated_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

        names = {f'#f{i}': k for i, k in enumerate(fields)}
        values = {f':v{i}': v for i, v in enumerate(fields.values())}
        update_expr = 'SET ' + ', '.join(f'#f{i} = :v{i}' for i in range(len(fields)))

        table.update_item(
            Key={'student_id': student_id.strip()},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression='attribute_exists(student_id)'
        )
        return respond(200, {'message': 'Cập nhật thành công!'})

    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return respond(404, {'error': 'Sinh viên này không tồn tại trong hệ thống!'})
        logger.exception('Lỗi DynamoDB khi cập nhật sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})
    except Exception:
        logger.exception('Lỗi không xác định khi cập nhật sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})