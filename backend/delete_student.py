import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

table = boto3.resource('dynamodb').Table('Students')
HEADERS = {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}


def respond(status, payload):
    return {'statusCode': status, 'headers': HEADERS, 'body': json.dumps(payload, ensure_ascii=False)}


def lambda_handler(event, context):
    try:
        query_params = event.get('queryStringParameters') or {}
        student_id = (query_params.get('student_id') or '').strip()

        if not student_id:
            return respond(400, {'error': 'Vui lòng cung cấp student_id cần xóa.'})

        table.delete_item(
            Key={'student_id': student_id},
            ConditionExpression='attribute_exists(student_id)'
        )
        return respond(200, {'message': f'Đã xóa thành công sinh viên {student_id}'})

    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return respond(404, {'error': 'Không thể xóa vì mã sinh viên này không tồn tại!'})
        logger.exception('Lỗi DynamoDB khi xóa sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})
    except Exception:
        logger.exception('Lỗi không xác định khi xóa sinh viên')
        return respond(500, {'error': 'Lỗi hệ thống, vui lòng thử lại sau.'})