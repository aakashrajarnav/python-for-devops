import boto3
import boto3.session

s3 = boto3.client('s3')
response = s3.list_buckets()

""" for key, value in response.items():
    if key == "Buckets":
        for bucket in value:
            print(f"Bucket: {bucket['Name']}")
    else:
        continue
"""

for bucket in response["Buckets"]:
    print(bucket["Name"])