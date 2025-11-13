import uuid

from cbt_redis.connection import get_redis_connection

def run_init():
    redis_connection = get_redis_connection()

    redis_connection.hset(f"cbt_startups:{str(uuid.uuid4())}", "success", str(True))