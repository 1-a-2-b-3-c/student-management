import json
import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj) if obj % 1 else int(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        query_params = event.get('queryStringParameters') or {}
        
        # Trường hợp 1: Tìm theo Khóa chính (student_id)
        if 'student_id' in query_params:
            response = table.get_item(Key={'student_id': query_params['student_id']})
            data = response.get('Item', {})
            
        # Trường hợp 2: Lọc theo Ngành học bằng GSI (major)
        elif 'major' in query_params:
            response = table.query(
                IndexName='major-index',
                KeyConditionExpression=Key('major').eq(query_params['major'])
            )
            data = response.get('Items', [])
            
        # Trường hợp 3: Lấy toàn bộ danh sách (Scan)
        else:
            response = table.scan()
            data = response.get('Items', [])
            
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(data, cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
