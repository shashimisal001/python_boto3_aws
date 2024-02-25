import boto3
import json


def create_policy():
    iam = boto3.client("iam")
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::shashitestbucket"
        }]
    }
    res = iam.create_policy(
        PolicyName="pyS3ObjectGetAccess",
        PolicyDocument=json.dumps(policy)
    )
    print(res)


create_policy()