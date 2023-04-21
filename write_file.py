import os
import sys

version = os.environ['Version']
data ='''import boto3
import os

client = boto3.client('datasync', region_name='us-east-1')

def lambda_handler(event,context):
    response = client.start_task_execution(
        TaskArn='arn:aws:datasync:us-east-1:135274860544:task/task-0c6a234345cc94d5f',
        Includes=[
            {}
                'FilterType': 'SIMPLE_PATTERN',
                'Value': '/{}'
            {},
        ]
    )
'''

file = open ('lambda_prueba.py', 'w')
file.write(data.format('{',version,'}'))
file.close()