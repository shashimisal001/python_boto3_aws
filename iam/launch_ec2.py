import boto3


def launch_ec2(instance_profile_name):
    ec2_client = boto3.client("ec2")
    res = ec2_client.run_instances(
        ImageId="ami-0e670eb768a5fc3d4",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1,
        IamInstanceProfile={
            "Name": instance_profile_name
        }
    )
    instance_id=res["Instances"][0]["InstanceId"]
    print(instance_id)


launch_ec2("test_instance_profile1")
