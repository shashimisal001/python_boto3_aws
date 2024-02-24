import boto3


def delete_login_profile(username):
    iam = boto3.client("iam")
    res = iam.delete_login_profile(UserName=username)
    print(res)


delete_login_profile("test_user1")
