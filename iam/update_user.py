import boto3


def update_user(old_username, new_username):
    iam = boto3.client("iam")
    res = iam.update_user(UserName=old_username,
                          NewUserName=new_username)
    print(res)


update_user("test_user", "test_user1")
