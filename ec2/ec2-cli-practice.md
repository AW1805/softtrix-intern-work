# EC2 Practice Using AWS CLI

## Find Latest Amazon Linux AMI

aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" \
--query "Images | sort_by(@, &CreationDate) | [-1].ImageId" \
--output text

This command retrieves the latest Amazon Linux AMI ID.

---

## Launch EC2 Instance

aws ec2 run-instances \
--image-id ami-0d16415f0e2dc4b80 \
--count 1 \
--instance-type t3.micro \
--region ap-south-1

Launches a new EC2 instance.

---

## Check Instance Status

aws ec2 describe-instances \
--query "Reservations[*].Instances[*].[InstanceId,State.Name]" \
--output table

Displays instance ID and current state.

---

## Terminate Instance

aws ec2 terminate-instances \
--instance-ids i-xxxxxxxxxxxx

Terminates the EC2 instance.

---

## Confirm Termination

aws ec2 describe-instances \
--instance-ids i-xxxxxxxxxxxx \
--query "Reservations[*].Instances[*].[State.Name]"

Confirms the instance has been terminated.
