import json
import boto3
from decimal import Decimal
from datetime import datetime, timezone
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'], parse_float=Decimal)
        
        student_id = body.pop('student_id', None)
        if not student_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Thiếu tham số student_id bắt buộc.'})
            }
        
        body['updated_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        
        update_expr = "SET "
        expr_attr_names = {}
        expr_attr_values = {}
        
        for key, value in body.items():
            update_expr += f"#{key} = :{key}, "
            expr_attr_names[f"#{key}"] = key
            expr_attr_values[f":{key}"] = value
            
        update_expr = update_expr.rstrip(', ')
        
        response = table.update_item(
            Key={'student_id': student_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=expr_attr_names,
            ExpressionAttributeValues=expr_attr_values,
            ConditionExpression="attribute_exists(student_id)", 
            ReturnValues="UPDATED_NEW"
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Cập nhật thành công!'})
        }
        
    except ClientError as e:
        # Bắt đúng lỗi do không thỏa mãn ConditionExpression (Sinh viên không tồn tại)
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return {
                'statusCode': 404,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Lỗi: Sinh viên này không tồn tại trong hệ thống!'})
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

