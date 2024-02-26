import boto3


def attach_role_to_instance_profile(instance_profile_name, role_name):
    iam = boto3.client("iam")
    res = iam.add_role_to_instance_profile(InstanceProfileName=instance_profile_name, RoleName=role_name)
    print(res)


attach_role_to_instance_profile("test_instance_profile1", "test_role1")
