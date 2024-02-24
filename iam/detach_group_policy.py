import boto3


def detach_group_policy(group_name, policy_arn):
    iam = boto3.client("iam")
    res = iam.detach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
    print(res)


detach_group_policy("S3Admins", "arn:aws:iam::aws:policy/AmazonS3FullAccess")