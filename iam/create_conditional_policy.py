import boto3
import json
from datetime import datetime


def create_conditional_policy():
    t1 = datetime.utcnow().strftime("%Y-%m-%d")+"T02:00:00Z"
    t2 = datetime.utcnow().strftime("%Y-%m-%d")+"T03:00:00Z"
    iam = boto3.client("iam")
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::shashitestbucket",
            "Condition": {
                "DateGreaterThan": {"aws:CurrentTime": t1},
                "DateLessThan": {"aws:CurrentTime": t2}
            }
        }]
    }
    res = iam.create_policy(
        PolicyName="pyConditionalS3GetObjectAccess",
        PolicyDocument=json.dumps(policy_document)
    )
    print(res)


create_conditional_policy()