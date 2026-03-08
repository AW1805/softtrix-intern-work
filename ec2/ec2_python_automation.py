import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="ap-south-1")

# Launch EC2 instance
response = ec2.run_instances(
    ImageId="ami-0d682f26195e9ec0f",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

instance_id = response["Instances"][0]["InstanceId"]
print("EC2 instance created:", instance_id)

# Check instance status
status = ec2.describe_instances(InstanceIds=[instance_id])
state = status["Reservations"][0]["Instances"][0]["State"]["Name"]
print("Current instance state:", state)

# Terminate instance
ec2.terminate_instances(InstanceIds=[instance_id])
print("EC2 instance terminated:", instance_id)
