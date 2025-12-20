from discord.message import Message

from utils.message_utils import get_all_urls_in_message
from utils.url_checks import is_site_paywalled, get_archive_of_site
from utils.utils import logger
from message_handlers import handler


@handler(name="depaywaller", has_urls=True)
async def depaywall(message: Message):
    urls = get_all_urls_in_message(message)

    logger.info(f"Found {len(urls)} urls")

    for url in urls:
        # Check if the site is paywalled
        if not is_site_paywalled(url):
            logger.info(f"{url} is not paywalled")
            continue

        logger.info(f"Found paywalled site: {url}")

        archive_of_site = get_archive_of_site(url)
        if archive_of_site is None:
            logger.info(f"No archive for {url} found :(")
            return

        await message.reply(
            f"Looks like you linked to a webpage which is possilby paywalled! The internet archive is cool and gets us around that, try and take a look here: {archive_of_site}. If this in error, go yell at Nick!"
        )
