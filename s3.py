import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

matching_buckets = []

tag_key = 'Env'
tag_value = 'Test'

for bucket in s3.list_buckets()['Buckets']:
    location = s3.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint']
    if location != 'sa-east-1' and location != 'us-west-2':
        try:
            tags = s3.get_bucket_tagging(Bucket=bucket['Name'])['TagSet']
            for tag in tags:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    #print(bucket['Name'])
                    matching_buckets.append(bucket['Name'])
                    print('S3 Buckets that does match to Tag Name', tag_value, 'are: ', matching_buckets)
        except ClientError:
            print(bucket['Name'], 'does not have tags')