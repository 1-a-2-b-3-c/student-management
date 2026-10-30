import json
import logging
import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)

table = boto3.resource('dynamodb').Table('Students')
HEADERS = {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj) if obj % 1 else int(obj)
        return super().default(obj)


def respond(status, payload):
    return {'statusCode': status, 'headers': HEADERS,
            'body': json.dumps(payload, cls=DecimalEncoder, ensure_ascii=False)}


def lambda_handler(event, context):
    try:
        params = event.get('queryStringParameters') or {}

        if 'student_id' in params:
            student_id = (params['student_id'] or '').strip()
            if not student_id:
                return respond(400, {'error': 'student_id không được để trống.'})
            item = table.get_item(Key={'student_id': student_id}).get('Item')
            if not item:
                return respond(404, {'error': 'Không tìm thấy sinh viên này!'})
            return respond(200, item)

        if 'major' in params:
            major = (params['major'] or '').strip()
            if not major:
                return respond(400, {'error': 'major không được để trống.'})
            response = table.query(
                IndexName='major-index',
                KeyConditionExpression=Key('major').eq(major)
            )
            items = response.get('Items', [])

        else:
            response = table.scan()
            items = response.get('Items', [])

        items.sort(key=lambda s: s.get('student_id', ''))
        return respond(200, items)

    except Exception:
        logger.exception('Lỗi khi truy vấn sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})