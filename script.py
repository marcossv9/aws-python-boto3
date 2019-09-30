import boto3
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

tag_key = 'Env'
input_tag_value = input('Enter tag values separated by commas:\n\n')
tag_values = input_tag_value.split(',')

# get a list of all instances
all_instances = ec2.instances.all()

print('\n\n\nChecking EC2 instances:\n\n\n')

# get instances with filter of running + with tag `Name`
for tag_value in tag_values:
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:' + tag_key, 'Values': [tag_value]}])
    for instance in instances:
        # make a list of filtered instances IDs `[i.id for i in instances]`
        # Filter from all instances the instance that are not in the filtered list
        instances_not_match = [not_match.id for not_match in all_instances if not_match.id not in [i.id for i in instances]]

print('EC2 Instances that do not match with Tag Values:\n\n',instances_not_match)


s3 = boto3.client('s3')

matching_buckets = []
notmatching_buckets = []
nottaged_buckets = []

print('\n\n\nChecking S3 Buckets:\n\n\n')

for bucket in s3.list_buckets()['Buckets']:
    bucketName = bucket['Name']
    location = s3.get_bucket_location(Bucket=bucketName)['LocationConstraint']
    if location == None:
        try:
            tags = s3.get_bucket_tagging(Bucket=bucketName)['TagSet']
            for tag in tags:
                for tag_value in tag_values:
                    if tag['Key'] == tag_key and tag['Value'] == tag_value:
                        if bucketName not in matching_buckets:
                            matching_buckets.append(bucketName)
                            notmatching_buckets.remove(bucketName)
                    elif tag['Key'] == tag_key and tag['Value'] != tag_value and bucketName not in matching_buckets:
                        if bucketName not in notmatching_buckets:
                            notmatching_buckets.append(bucketName)
        except ClientError:
            nottaged_buckets.append(bucketName)
print('S3 Buckets that match to Tag Values', tag_values, 'are: ', matching_buckets)
print('S3 Buckets that do not match to Tag Values', tag_values, 'are: ', notmatching_buckets)
print('S3 Buckets that do not have Tags are: ', nottaged_buckets)