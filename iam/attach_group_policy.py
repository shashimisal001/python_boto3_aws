import boto3


def attach_group_policy(group_name, policy_arn):
    iam = boto3.client("iam")
    res = iam.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
    print(res)


attach_group_policy("test_users", "arn:aws:iam::aws:policy/AmazonS3FullAccess")
