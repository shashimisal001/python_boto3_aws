import boto3


def all_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_users")
    for response in paginator.paginate():
        for user in response["Users"]:
            tags = iam.list_user_tags(UserName=user["UserName"])
            print("Username: {}, Tags: {}".format(user['UserName'], tags['Tags']))


all_users()
