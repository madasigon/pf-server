from io import BytesIO as B

import boto3
from botocore.client import Config

from instance.config import S3


def ct(name):
    return dict(
        html = "text/html"
    ).get(name.split(".")[-1], "binary/octet-strean")
session = boto3.session.Session()
client = session.client('s3',**S3.access)

def new_file(name, content, public=True):    
    client.upload_fileobj(
        B(content.encode('utf-8')),
        S3.bucket,
        name,
        ExtraArgs = dict(
            ACL = "public-read" if public else 'private',
            ContentType=ct(name)
        )
    )
