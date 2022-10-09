import os


def get_token():
    if os.environ.get("DISCORD_TOKEN", None) is None:
        print("ERROR: INVALID TOKEN")
        exit(1)
    return os.environ.get("DISCORD_TOKEN", None)
