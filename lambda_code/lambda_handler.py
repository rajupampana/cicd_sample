import json


def handler(event, context):

    print("Lambda Function Created from GIT Success")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }