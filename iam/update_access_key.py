import boto3


def update_access_key(username, access_key_id):
    iam = boto3.client("iam")
    res = iam.update_access_key(
        UserName=username,
        AccessKeyId=access_key_id,
        Status="Inactive"
    )
    print(res)


update_access_key("test_user1", "AKIAU6GDWKHPFTAV3E4P")