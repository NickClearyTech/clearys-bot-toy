import random
from discord.message import Message
from message_handlers import handler

emacs_quotes_options = [
    "eMaCS Is THe BEsT tExt edIToR",
    "Have you considered trying nvim?",
    "FYI: package update 1.69 is now available for Deldo. Resolves numerous bugs with the Thurstmaster series' integration",
    "emacs? Is that like an off brand iMac?",
    "*spends 80 hours a week configuring text editor*",
    "Dror ragzlin... dror ragzlin... had a warrior's heart. And a killer emacs config.",
    "Richard, have you reminded Nick to try out Neovim today? If not, you should. If you have, you should again. Just to be sure."
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
