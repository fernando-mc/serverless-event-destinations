import json


def starting(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def success(event, context):
    print("success")
    print(event)

def failure(event, context):
    print("failed")
    print(event)