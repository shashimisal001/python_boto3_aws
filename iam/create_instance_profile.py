import boto3


def create_instance_profile(instance_profile_name):
    iam = boto3.client("iam")
    res = iam.create_instance_profile(InstanceProfileName=instance_profile_name)
    print(res)


create_instance_profile("test_instance_profile1")