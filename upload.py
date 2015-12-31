"""
This module provides a helper method for uploading files to S3.
"""

import boto3
import os
from logger import logger

# To communicate with S3, the following environment variables need to be set:
# - AWS_ACCESS_KEY_ID
# - AWS_SECRET_ACCESS_KEY
# - S3_BUCKET
# The bucket specified in the latter should already be created.
BUCKET = os.environ['S3_BUCKET']

s3 = boto3.resource('s3')

def upload_file(local_path):
    """
    Upload the given file to S3

    The file will be placed at the top level of the bucket, keeping its name the same.

    By using boto3's `upload_file` method from the "S3 customization," we get
    these features for free:
    - Automatically switching to multipart transfers when a file is over a specific size threshold
    - Throttling based on max bandwidth
    - Retries
    """
    remote_name = os.path.basename(local_path)
    logger.info('Uploading file %s to %s as %s' % (local_path, BUCKET,
        remote_name))
    s3.meta.client.upload_file(local_path, BUCKET, remote_name)

def upload_and_delete_file(path):
    """
    Upload the given file to S3, then remove it from the local filesystem
    """
    upload_file(path)
    logger.info('Upload complete. Deleting %s' % path)
    os.remove(path)
