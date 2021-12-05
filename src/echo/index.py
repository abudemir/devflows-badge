import json
import logging

from src.output_formatter import get_success_output, get_error_output

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


"""
Write your code here.
"""
def handler(event, context):

    logger.info("Context enabled Echo invocable")
    try:
        body = json.loads(event)['body']
        result = list()
        return get_success_output(200, body)
    except:
        return get_error_output(500, "Dummy error message", "Internal Server Error")
