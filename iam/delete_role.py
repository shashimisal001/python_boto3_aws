import boto3


def delete_role(role_name):
    iam = boto3.client("iam")
    res = iam.delete_role(RoleName=role_name)
    print(res)


delete_role("test_role1")