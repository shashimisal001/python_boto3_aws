import boto3
import json


def create_role():
    iam = boto3.client("iam")
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }]
    }
    res = iam.create_role(
        RoleName="test_role1",
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    print(res)

create_role()