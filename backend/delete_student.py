import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    try:
        query_params = event.get('queryStringParameters') or {}
        
        if 'student_id' not in query_params:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Vui lòng cung cấp student_id cần xóa.'})
            }
            
        student_id = query_params['student_id']
        
        table.delete_item(
            Key={'student_id': student_id},
            ConditionExpression="attribute_exists(student_id)"
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': f'Đã xóa thành công sinh viên {student_id}'})
        }
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return {
                'statusCode': 404,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Lỗi: Không thể xóa vì mã sinh viên này không tồn tại!'})
            }
        else:
            return {
                'statusCode': 500,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': str(e)})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }