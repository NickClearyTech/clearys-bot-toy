import random
from discord.message import Message
from message_handlers import handler
from utils import emacs

emacs_quotes_options = [
    # Due to limitations with Emacs string concatenation in the manner
    # we're invoking it, "" and apostrophe characters cannot be
    # embedded in strings.
    emacs.emacs_concat_all_the_strings(["eMaCS", "Is", "THe", "BEsT", "tExt", "edIToR"], sep=" "),
    emacs.emacs_concat_all_the_strings(["Have", "you", "considered", "trying", "nvim?"], sep=" "),
    emacs.emacs_concat_all_the_strings(["FYI:", "package", "update", "1.69", "is", "now", "available", "for", "Deldo.",
                                        "Resolves", "numerous", "bugs", "with", "the", "Thurstmaster", "series", "integration"], sep=" "),
    emacs.emacs_concat_all_the_strings(["emacs?", "Is", "that", "like", "an", "off", "brand", "iMac?"], sep=" "),
    emacs.emacs_concat_all_the_strings(["*spends", "80", "hours", "a", "week", "configuring", "text", "editor*"], sep=" "),
    emacs.emacs_concat_all_the_strings(["Dror", "ragzlin...", "dror", "ragzlin...", "had", "a", "warriors", "heart.", "And", "a", "killer", "emacs", "config."], sep=" "),
    emacs.emacs_concat_all_the_strings(["Richard,", "have", "you", "reminded", "Nick", "to", "try", "out", "Neovim", "today?",
                                        "If", "not,", "you", "should.",
                                        "If", "you", "have,", "you", "should", "again.",
                                        "Just", "to", "be", "sure."], sep=" "),
    emacs.emacs_concat_string("Using the power of Emacs, you can add arbitrary code execution features to any repo! This meme was generated on: \" (current-time-string)", "\"")
]

guix_quotes_option = [
    "I was not installed using GNU Guix unfortunately. Please open an issue on my repository to request it, and open a PR to make it happen.",
    "Docker > Guix. You may not like it, but it's the truth. Are they even directly competing standards? No. Do I care? No.",
    "What does Guix even stand for anyway? Greater Ulysses Is Xenophobic?",
    "Real men use Gentoo. Just saying.",
    "guix package -i happiness\nFuck that didn't work.",
    "I packaged Windows XP as a guix package. Because I can. Some men just want to watch the world burn."
]


# A bot handler to reply with "THE PROPHET HAS SPOKEN" whenever richard mentions emacs in the emacs channel
@handler(
    name="Prophet has spoken", channels=[992166504269357146], users=[192024972644974592]
)
async def prophet_has_spoken(message: Message):
    if "emacs" in message.content.lower():
        await message.reply("*THE PROPHET HAS SPOKEN*")


@handler(name="Emacs quotes", users=[192024972644974592])
async def emacs_quotes(message: Message):
    if "emacs" in message.content.lower() and random.randint(1, 10) > 3:
        await message.reply(random.choice(emacs_quotes_options))


@handler(name="Guix Quotes", users=[192024972644974592])
async def guix_quotes(message: Message):
    if "guix" in message.content.lower() and random.randint(1, 10) > 3:
        await message.reply(random.choice(guix_quotes_option))
