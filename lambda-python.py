
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
  USERNAME = event['USERNAME']
  EMAIL = event['EMAIL']
  PASSWORD = event['PASSWORD']
  DETAILS = event['DETAILS']
  dynamodb.put_item(TableName='My-User-Table', Item={'USERNAME':{'S':USERNAME},'EMAIL':{'S':EMAIL},'PASSWORD':{'S':PASSWORD},'DETAILS':{'S':DETAILS}})
  print(EMAIL)
