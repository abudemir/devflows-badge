import json
import logging

from src.output_formatter import get_error_output

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

 
"""
Write your code here.
"""
def handler(event, context):
    try:
        body = json.loads(event)['body']
        response = {
            'statusCode': 200,
            'request_id': body['request_id'],
            'fields': body['event']['fields'],
            'body': body
        }

        return response
    except:
        return get_error_output(500, "Dummy error message", "Internal Server Error")