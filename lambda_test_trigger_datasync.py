import boto3
import sys

#client = boto3.client('datasync', region_name='us-east-1')

# def lambda_handler(event,context):
#     response = client.start_task_execution(
#         TaskArn='arn:aws:datasync:us-east-1:135274860544:task/task-0c6a234345cc94d5f',
#         Includes=[
#             {
#                 'FilterType': 'SIMPLE_PATTERN',
#                 'Value': '/4.50.0'
#             },
#         ]
#     )

print (sys.argv[0])