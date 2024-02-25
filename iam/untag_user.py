import boto3


def untag_user(username):
    iam = boto3.client("iam")
    tag_keys = ["Department", "Designation"]
    res = iam.untag_user(
        UserName=username,
        TagKeys=tag_keys
    )
    print(res)


untag_user("test_user1")