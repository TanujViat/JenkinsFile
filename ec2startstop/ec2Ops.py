import sys
import boto3

def ec2Ops(action, instance_id, aws_access_key_id, aws_secret_access_key, aws_region):
    print("Inside Fucntion")
    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )
    if action == 'start':
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f'Instance {instance_id} started')
    elif action == 'stop':
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f'Instance {instance_id} stopped')
    else:
        print('Invalid action. Use "start" or "stop".')

if __name__ == "__main__":
    print("Hiiii")
    action1 = sys.argv[1]
    print("Action", action1)
    instance_id = sys.argv[2]
    aws_access_key_id = sys.argv[3]
    aws_secret_access_key = sys.argv[4]
    aws_region = sys.argv[5]
    ec2Ops(action1, instance_id, aws_access_key_id, aws_secret_access_key, aws_region)
