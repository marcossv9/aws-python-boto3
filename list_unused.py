import boto3
#import sys

tagkey = input("Enter Tag Name to find: ")
tagvalue = input("Enter Tag Value to find: ")
print('\n')
print('List of instances that dont match with Tags:')

ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:'+tagkey,
            'Values': [tagvalue]
        }
    ]
)
instancelist = []
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        instancelist.append(instance["InstanceId"])
print(instancelist)
print('\n')
print('List of buckets that dont match with Tags:')