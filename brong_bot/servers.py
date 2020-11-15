import logging
from enum import Enum

import boto3
from botocore.exceptions import ClientError


class EC2_Instances(Enum):
    Factorio = "i-087a963bf6f1e8f21"
    Minecraft = "i-08603abb89172582b"


def startServer(ec2_instance: EC2_Instances):
    ec2 = boto3.resource("ec2", "us-west-2")

    try:
        instance = ec2.Instance(id=ec2_instance.value)
        instance.start()
        instance.wait_until_running()
        return instance.public_dns_name
    except ClientError as e:
        logging.error(e)


def stopServer(ec2_instance: EC2_Instances):
    ec2 = boto3.resource("ec2", "us-west-2")
    try:
        instance = ec2.Instance(id=ec2_instance.value)
        instance.stop()
    except ClientError as e:
        logging.error(e)
