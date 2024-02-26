import boto3


def list_policies():
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_policies")
    for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            print("PolicyName: {}, Arn: {}".format(policy["PolicyName"], policy["Arn"]))


list_policies()