import boto3
client = boto3.client('ec3')
response = client.run_instances(
     ImageId='ami-068e0f1a600cd311c',
     InstanceType='t2.micro',
     KeyName='public',
     MaxCount=1,
     MinCount=1

)
