import boto3


def attach_role_policy(role_name, policy_arn):
    iam = boto3.client("iam")
    res = iam.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
    print(res)


attach_role_policy("test_role1", "arn:aws:iam::339712823774:policy/pyS3ObjectGetAccess")
