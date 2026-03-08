# Goal: Perform basic S3 operations using Python (boto3)
# Operations: Create bucket → Upload file → Delete file → Delete bucket

import boto3

# Configuration
region = "ap-south-1"
bucket_name = "demo-s3-bucket-2026"
local_file_path = "simple.txt"
object_name = "simple.txt"

# Create S3 client
s3 = boto3.client("s3", region_name=region)

# Create S3 Bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": region}
)

print("S3 bucket created:", bucket_name)

# Upload file to S3
s3.upload_file(local_file_path, bucket_name, object_name)
print("File uploaded:", object_name)

# Delete file from S3
s3.delete_object(
    Bucket=bucket_name,
    Key=object_name
)

print("File deleted:", object_name)

# Delete S3 bucket
s3.delete_bucket(Bucket=bucket_name)
print("S3 bucket deleted:", bucket_name)
