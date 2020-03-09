import json


def starting(event, context):
    if event["Success"] == True:
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response
    else:
        print("Time to fail!")
        raise Exception("Some serious failure")


def success(event, context):
    print("success")
    print(event)


def failure(event, context):
    print("failed")
    print(event)