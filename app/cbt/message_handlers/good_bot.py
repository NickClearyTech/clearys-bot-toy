from message_handlers import handler
from discord.message import Message


@handler(name="Good Bot")
async def handle_good_bot(message: Message):
    if message.content.casefold() == "Good bot".casefold():
        await message.reply("Thanks Daddy. I try.")
