import base64
import logging

import boto3
from botocore.exceptions import ClientError


SECRET_NAME = "BrongBot/DiscordToken"


def get_discord_api_key():
    client = boto3.client('secretsmanager')

    try:
        response = client.get_secret_value(SecretId=SECRET_NAME)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        logging.error("Failed to get discord api_key %s", error_code)
    else:
        if "SecretString" in response:
            return response["SecretString"]
        else:
            return base64.b64decode(
                response["SecretBinary"]
            )
