import boto3


def attach_policy(username, policy_arn):
    iam = boto3.client("iam")
    res = iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    print(res)


attach_policy("test_user1", "arn:aws:iam::aws:policy/AmazonRDSFullAccess")