import boto3


def create_access_key(username):
    iam = boto3.client('iam')
    res = iam.create_access_key(UserName=username)
    print(res)


create_access_key("test_user1")