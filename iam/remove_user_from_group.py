import boto3


def remove_user_from_group(username, group_name):
    iam = boto3.client("iam")
    res = iam.remove_user_from_group(
        UserName=username,
        GroupName=group_name
    )
    print(res)


remove_user_from_group("test_user1", "test_users")
