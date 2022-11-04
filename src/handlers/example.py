from utils.networking import response


def handler(event, context):
    body = {
        "message": "You have successfully requested a GET"
    }
    return response(status=200, body=body)