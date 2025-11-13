import os

from utils.utils import logger

from cbt_minio.connection import get_minio_client

def validate_minio_bucket_exists():
    logger.debug("Validating Minio connection")
    minio_client = get_minio_client()
    minio_client.bucket_exists(os.getenv("MINIO_BUCKET_NAME"))
    logger.info(f"Validated s3 bucket {os.getenv('MINIO_BUCKET_NAME')} exists")