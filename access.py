import json
import boto3

s3_client = boto3.client('s3')
bucket_name = 'demo-bucket-acs'
object_key = 'version.json'
response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
json_data = json.loads(response['Body'].read().decode('utf-8'))
access_value = json_data["image_version"]
print(access_value)