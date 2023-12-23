import os


def get_token():
    if os.environ.get("DISCORD_TOKEN", None) is None:
        print("ERROR: INVALID TOKEN")
        exit(1)
    return os.environ.get("DISCORD_TOKEN", None)


# Wraps a set of text in a code block
# This avoid issues with double slashes \\, that the discord util escape markdown does not handle
def codeify(text: str):
    return f"```{text}```"
