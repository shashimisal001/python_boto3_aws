import boto3


def delete_policy(policy_arn):
    iam = boto3.client("iam")
    res = iam.delete_policy(PolicyArn=policy_arn)
    print(res)


delete_policy("arn:aws:iam::339712823774:policy/pyFullAccess")