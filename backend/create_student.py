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
        if f not in data or not data[f].strip():
            return f'Thiếu trường bắt buộc: {f}'
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
    if 'is_active' in data and not isinstance(data['is_active'], bool):
        return 'is_active phải là true hoặc false.'
    return None


def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body') or '', parse_float=Decimal)
        
        student_id = body.get('student_id')
        if not isinstance(student_id, str) or not student_id.strip():
            return respond(400, {'error': 'Thiếu student_id bắt buộc.'})

        error = validate(body)
        if error:
            return respond(400, {'error': error})

        now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        item = {k: (body[k].strip() if isinstance(body[k], str) else body[k]) for k in FIELDS if k in body}
        item.update({'student_id': student_id.strip(), 'created_at': now, 'updated_at': now})

        table.put_item(Item=item, ConditionExpression='attribute_not_exists(student_id)')
        return respond(201, {'message': 'Thêm sinh viên thành công!', 'student_id': item['student_id']})

    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return respond(409, {'error': 'Mã sinh viên này đã tồn tại!'})
        logger.exception('Lỗi DynamoDB khi tạo sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})
    except Exception:
        logger.exception('Lỗi không xác định khi tạo sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})