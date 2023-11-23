from message_handlers import handler
from discord.message import Message


@handler(name="Good Bot")
async def handle_good_bot(message: Message):
    if message.content.lower() == "good bot":
        await message.reply("Thanks Daddy. I try.")
