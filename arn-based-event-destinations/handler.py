import json


def starting(event, context):
    if event["Success"] == True:
        response = {
            "statusCode": 200,
            "body": json.dumps(event)
        }
        return response
    else:
        print("Time to fail!")
        raise Exception("Some serious failure")
