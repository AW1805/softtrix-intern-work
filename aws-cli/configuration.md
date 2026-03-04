# AWS CLI Configuration

Configured AWS CLI on my macOS system so I could interact with AWS services through the terminal.

### Command used

aws configure

Entered the following details when prompted:

Access Key ID  
Secret Access Key  
Region: ap-south-1  
Output format: json

### Verification

To verify that the CLI was configured correctly, I ran:

aws sts get-caller-identity

This returned my AWS account ID and IAM user ARN, confirming that the CLI was connected successfully.
