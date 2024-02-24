import boto3


def create_group(group_name):
    iam = boto3.client("iam")
    res = iam.create_group(GroupName=group_name)
    print(res)


create_group("test_users")
