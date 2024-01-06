from config.get_config import config_object
import aiohttp
from utils.utils import logger


async def get_languages() -> dict:
    async with aiohttp.ClientSession(
        base_url=config_object.libretranslate_server_config.url
    ) as session:
        languages: list
        async with session.get("/languages") as response:
            match response.status:
                case 200:
                    logger.debug(f"Got response from {response.real_url}")
                    try:
                        languages = await response.json()
                    except Exception as e:
                        logger.error(f"Failed to fetch languages with error {e}")
                        raise e
                case _:
                    logger.error(
                        f"Call to {response.real_url} failed with error code {response.status}"
                    )
                    logger.debug(await response.json())
                    raise ConnectionError(
                        f"Call to {response.real_url} failed with error code {response.status}"
                    )

        if len(languages) == 0:
            logger.error("Failed to find any languages")
            raise ConnectionError(
                f"Call to {response.real_url} failed to fetch languages"
            )

        # build language dict
        languages_dict = {
            language["code"]: {"name": language["name"], "targets": language["targets"]}
            for (language) in languages
        }

        return languages_dict


async def translate_text(
    text: str, target_language_in: str = None, source_language_in: str = "auto"
) -> str:
    if target_language_in is None:
        return text
    target_language: str = target_language_in.casefold()
    source_language: str = source_language_in.casefold()
    logger.info(f"Invoking translator {source_language}->{target_language}")

    async with aiohttp.ClientSession(
        base_url=config_object.libretranslate_server_config.url
    ) as session:
        real_source_language = "en"
        if source_language == "auto":
            async with session.post("/detect", json={"q": text}) as response:
                match response.status:
                    case 200:
                        logger.debug(f"Got response from {response.real_url}")
                        try:
                            real_source_language = (await response.json())[0][
                                "language"
                            ]
                        except Exception as e:
                            logger.error(
                                f"Failed to set source language with error {e}"
                            )
                            logger.debug(await response.json())
                    case _:
                        logger.error(
                            f"Call to {response.real_url} failed with error code {response.status}"
                        )
                        logger.debug(await response.json())

        languages = await get_languages()

        if real_source_language not in languages.keys():
            logger.error(f"Recieved invalid source language {real_source_language}")
            return text

        if target_language not in languages[real_source_language]["targets"]:
            logger.error(
                f"Recieved invalid target language {target_language} for source language {real_source_language}"
            )
            return text

        async with session.post(
            "/translate",
            json={
                "q": text,
                "source": real_source_language,
                "target": target_language,
                "format": "text",
            },
        ) as response:
            match response.status:
                case 200:
                    logger.debug(f"Got response from {response.real_url}")
                    try:
                        return (await response.json())["translatedText"]
                    except Exception as e:
                        logger.error(f"Failed to get translated text with error {e}")
                        return text
                case _:
                    logger.error(
                        f"Call to {response.real_url} failed with error code {response.status}"
                    )
                    logger.debug(await response.json())
                    return text


# Wraps a set of text in a code block
# This avoid issues with double slashes \\, that the discord util escape markdown does not handle
def codeify(text: str):
    return f"```{text}```"
