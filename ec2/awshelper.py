import boto3
from lp_aws import *
print(aws_access_key_id_value)
print(aws_secret_access_key_value)
print(region_name)

def describe_instances():
    import boto3

    # Create an EC2 client
    ec2_client = boto3.client('ec2',
                   aws_access_key_id=aws_access_key_id_value,
                   aws_secret_access_key=aws_secret_access_key_value,
                   region_name=region_name)

    # Describe all instances
    response = ec2_client.describe_instances()

    # Extract and print instance information
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("Instance ID:", instance['InstanceId'])
            print("Instance Type:", instance['InstanceType'])
            print("State:", instance['State']['Name'])
            print("Public IP Address:", instance.get('PublicIpAddress', 'N/A'))
            print("Private IP Address:", instance.get('PrivateIpAddress', 'N/A'))
            print("Launch Time:", instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S'))
            print("----------------------------")
