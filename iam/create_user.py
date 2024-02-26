import boto3


def create_user(username):
    iam = boto3.client('iam')
    res = iam.create_user(UserName=username)
    print(res)


create_user("test_user2")
