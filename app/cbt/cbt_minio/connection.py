import os

from minio import Minio


def get_minio_client():
    endpoint = os.environ.get("MINIO_ENDPOINT")
    access_key = os.environ.get("MINIO_ACCESS_KEY")
    secret_key = os.environ.get("MINIO_SECRET_KEY")
    secure = bool(os.environ.get("MINIO_SSL"))
    return Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=False)
