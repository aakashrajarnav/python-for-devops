import boto3

def get_connection(service):
    return boto3.client(service) # creating a client for S3 so that it can call APIs

def show_buckets(s3_client):
    response = s3_client.list_buckets()

    for bucket in response["Buckets"]:
        print(bucket["Name"])

def create_bucket(s3_client, bucket_name):
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name, 
            CreateBucketConfiguration={
                'LocationConstraint': 'us-west-2',
            },)
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("Bucket created successfully")
        else:
            print("Error occurred while creating the bucket")

    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_to_bucket(s3_client, file_path, bucket_name, key_name):
    s3_client.upload_file(file_path, bucket_name, key_name)
    print("File uploaded successfully")

def show_regions(ec2_client):
    response = ec2_client.describe_regions()
    for region in response['Regions']:
        print(region['RegionName'])

s3 = get_connection('s3')
ec2 = get_connection('ec2')

show_buckets(s3)
#create_bucket(s3, 'my-second-bucket-aakash-raj-12345')
upload_to_bucket(s3, 'output1.json', 'aakash-s3-first-bucket', 'output.json')
#show_regions(ec2)