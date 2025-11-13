import os

import redis


def get_redis_connection():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=os.getenv("REDIS_PORT", 6379),
        db=os.getenv("REDIS_DATABASE", 0),
        password=os.getenv("REDIS_PASSWORD", None),
    )
