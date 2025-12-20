import requests
import json
from typing import Optional
from bs4 import BeautifulSoup
from utils.utils import logger
from urllib.parse import urlparse


KNOWN_PAYWALLED_DOMAINS = [
    "wsj.com",
    "washingtonpost.com",
    "nytimes.com",
    "economist.com",
]


def get_archive_of_site(url: str) -> Optional[str]:
    """
    Attempt to get the archived version of a URL
    """
    response = requests.get(f"http://archive.org/wayback/available?url={url}")

    if not response.ok:
        return None
    logger.info(response.text)

    result = response.json()
    if "archived_snapshots" not in result:
        logger.error(f"Error getting archive of {url}, key not valid")
        return None

    if "closest" not in result["archived_snapshots"]:
        logger.error(f"Error getting archive of {url}, closest key not valid")
        return None

    return result["archived_snapshots"]["closest"]["url"]


def is_known_paywalled_domain(url: str) -> bool:
    """
    Check whether the given url's domain is a known paywalled domain
    """
    domain = urlparse(url).netloc
    # Remove the www. from the domain so we don't have to list every variation of each domain
    stripped_domain = (
        domain.replace("www.", "", 1) if domain.startswith("www.") else domain
    )
    return stripped_domain in KNOWN_PAYWALLED_DOMAINS


def is_site_paywalled(url):
    """
    Try and determine if the given url is a paywalled site
    First we try and access the site, and check for the isAccessibleForFree flag
    If we can't get that, whether the flag doesn't exist or we can't access the site due to captcha
    Then we just check if the sites domain is in the list of known paywalled domains
    """
    # Create a session and get the page
    session = requests.Session()
    response = session.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"
        },
    )

    # Get the soup :)
    soup = BeautifulSoup(response.text, "lxml")
    # Find all json info data used by scrapers
    results = soup.find_all("script", type="application/ld+json")

    for result in results:
        json_data = json.loads(result.text)
        # Skip any result whose data is a list, those aren't what we're looking for
        if isinstance(json_data, list):
            continue
        if (
            "isAccessibleForFree" in json_data.keys()
            and not json_data["isAccessibleForFree"]
        ):
            return True

    return is_known_paywalled_domain(url)
