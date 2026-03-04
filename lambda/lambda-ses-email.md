# AWS Lambda + SES Email

After verifying my email in Amazon SES, I created a Lambda function to send an email using Python.

### Create IAM Role

Created an IAM role for Lambda with the **AmazonSESFullAccess** policy so the function could send emails through SES.

### Create Lambda Function

1. Open AWS Console  
2. Go to **Lambda**  
3. Click **Create Function**  
4. Choose **Author from scratch**  
5. Runtime: **Python**  
6. Attach the IAM role created earlier to the execution role

### Lambda Code

The Lambda function uses **boto3** to send an email using Amazon SES.

```python
import boto3

def lambda_handler(event, context):
    ses = boto3.client('ses', region_name='ap-south-1')
    response = ses.send_email(
        Source='verified-sender@example.com',
        Destination={
            'ToAddresses': ['verified-recipient@example.com']
        },
        Message={
            'Subject': {
                'Data': 'Test Email from AWS Lambda'
            },
            'Body': {
                'Text': {
                    'Data': 'Hello,\n\nThis is a simple email sent using AWS Lambda and Amazon SES.'
                }
            }
        }
    )

    print("Email sent! Response:", response)

    return {
        'statusCode': 200,
        'body': 'Email sent successfully'
    }
