import random
from typing import List

from discord.message import Message
from message_handlers import handler
from config.get_config import config_object
from utils.utils import get_chance
from utils.utils import logger

caustic_memes: List[str] = [
    "Caustic? I think you mean Caus-too-thicc-for-me",
    "Conduit is better. You may be not like it, but it's the truth. Time to acknowledge it.",
    "Careful now. You don't want to trigger Shadi by mentioning the cursed character. Shhhh calming Watson noises",
    "Remember when Caustic was good? Pepperidge farm remembers.",
    "Cause these booty cheeks be clappin",
    "Pathfinder is trying to find a path to Caustics thicc ass",
]

taylor_memes: List[str] = [
    "Guys did you know Christen browses r/taylorswift? I think he's secretly a swiftie",
    "Classified intelligence indicates that Christen is obsessed with Taylor Swift and is jealous that he can't marry her",
    "State sponsored actors (Christen) have been known to drag Taylor's name through the mud. Fight back! Mud him!",
    "Imagine hating Tay Tay. Christen can. SMH",
]


@handler(
    name="Christen Mentions Causthicc",
    channels=config_object.all_memes_config.caustic.channels,
    users=config_object.all_memes_config.caustic.users,
)
async def christen_mentions_caustic(message: Message):
    if "caustic".casefold() in message.content.casefold() and get_chance():
        await message.reply(random.choice(caustic_memes))


@handler(
    name="Christen mentions his one true love, Chris",
    channels=config_object.all_memes_config.chris.channels,
    users=config_object.all_memes_config.chris.users,
)
async def christen_mentions_chris(message: Message):
    if "chris".casefold() in message.content.casefold():
        # React with the chris emoji
        for emoji in message.guild.emojis:
            if emoji.name == "chris":
                await message.add_reaction(emoji)
        await message.add_reaction("❤️")
        await message.add_reaction("🍆")
        await message.add_reaction("🥵")


@handler(
    name="Christen mentions Tay Tay", users=config_object.all_memes_config.taytay.users
)
async def christen_loves_taylor(message: Message):
    if "taylor".casefold() in message.content.casefold() and get_chance(percent=70):
        await message.reply(random.choice(taylor_memes))
