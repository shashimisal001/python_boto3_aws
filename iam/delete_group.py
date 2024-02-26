import boto3


def delete_user_group(group_name):
    iam = boto3.client("iam")
    res = iam.delete_group(GroupName=group_name)
    print(res)


delete_user_group("S3Admins")
