"""
Networking utility functions to support serverless application design
"""
from http.client import SERVICE_UNAVAILABLE, UNAUTHORIZED
from typing import Union, JSON
from enum import Enum, auto
from datetime import datetime

class StatusCode(Enum):
    """Enumerate REST response status codes"""
    SUCCESS = 200
    # Client Side Errors
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    # Server side errors
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503


# Define the response details of error messages
ErrorMessages = {
    StatusCode.BAD_REQUEST : {
        'message': "",
        'detail': "",
        'help': ""
    },
    StatusCode.UNAUTHORIZED : {
        'message': "",
        'detail': "",
        'help': ""
    },
    StatusCode.FORBIDDEN : {
        'message': "",
        'detail': "",
        'help': ""
    },
    StatusCode.NOT_FOUND : {
        'message': "",
        'detail': "",
        'help': ""
    },
    StatusCode.INTERNAL_SERVER_ERROR : {
        'message': "",
        'detail': "",
        'help': ""
    },
    StatusCode.SERVICE_UNAVAILABLE : {
        'message': "",
        'detail': "",
        'help': ""
    },
}

def response(status: Union[int, StatusCode], body) -> JSON:
    """
    Creates a reponse object from statuscode and message.
    """
    # Enable handling of multiple errors
    if isinstance(status, int):
        status = StatusCode[status]
    # Handle success case
    if status.value < 300:
        body = body
    else:
        body = compile_error(status, body)
    return {
        'status': status,
        'body': body
    } 

def compile_error(status: StatusCode, event, message: Exception) -> JSON:
    """
    Compile an error message based on the status code and message type
    """
    # Enable handling of multiple errors
    error = ErrorMessages[StatusCode]

    response = {
        "timestamp": str(datetime.now()),
        "error": StatusCode.value(),
        "message": error.get('error', 'Undefined error'),
        "path": event,
    }
    if 'detail' in error:
        response['detail'] = error['detail']
    if 'help' in error:
        response['help'] = error['help']