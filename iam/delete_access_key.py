import boto3


def delete_access_key(username, access_key_id):
    iam = boto3.client("iam")
    res = iam.delete_access_key(UserName=username, AccessKeyId=access_key_id)
    print(res)


delete_access_key("test_user1", "AKIAU6GDWKHPFTAV3E4P")