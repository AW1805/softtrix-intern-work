# Goal: To automate the running status of instances (servers) using lambda.
import boto3

ec2 = boto3.client('ec2')

DEV_INSTANCE = "i-0b86dc1fcf75599b0"
PROD_INSTANCE = "i-0561000cecaa889bd"

def lambda_handler(event, context):

    ec2.stop_instances(
        InstanceIds=[DEV_INSTANCE]
    )

    ec2.start_instances(
        InstanceIds=[PROD_INSTANCE]
    )

    return {
        'statusCode': 200,
        'body': 'Dev stopped and Prod started successfully'
     }
