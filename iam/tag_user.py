import boto3

def tag_user(username):
    iam = boto3.client("iam")
    tags = [{"Key": "Department", "Value": "Software"}, {"Key": "Designation", "Value": "Technology Specialist"}]
    res = iam.tag_user(UserName=username, Tags=tags)
    print(res)


tag_user("test_user1")