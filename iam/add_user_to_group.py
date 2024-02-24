import boto3


def add_user_to_group(username, group_name):
    iam = boto3.client("iam")
    res = iam.add_user_to_group(UserName=username, GroupName=group_name)
    print(res)


add_user_to_group("test_user1", "test_users")