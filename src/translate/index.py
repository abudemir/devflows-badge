import json
import logging
import boto3

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

        client = boto3.client('translate', region_name="us-east-1")

        if body["originalLanguageCode"] in ["en", "ar", "zh", "fr", "de", "hi", "it", "ja","ko", "pt", "ru","es"]:
            for lang in body["translationLanguages"]:
                print(lang)
                resp = client.translate_text(
                    Text=body["text"], 
                    SourceLanguageCode=body["originalLanguageCode"], 
                    TargetLanguageCode=lang
                )
                result.append({
                "translatedText" : resp["TranslatedText"],
                "language": lang
                })

        return get_success_output(200, {"result": result})
    except:
        return get_error_output(500, "Dummy error message", "Internal Server Error")
