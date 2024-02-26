import boto3


def detach_policy(username, policy_arn):
    iam = boto3.client("iam")
    res = iam.detach_user_policy(UserName=username, PolicyArn=policy_arn)
    print(res)


detach_policy("test_user1", "arn:aws:iam::339712823774:policy/pyFullAccess")
