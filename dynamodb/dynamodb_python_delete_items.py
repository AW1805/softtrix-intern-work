# Goal: To delete items in table.
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('DemoTable')

response = table.delete_item(
    Key={
        'UserID': '123'
    }
)

print("Item deleted successfully")
