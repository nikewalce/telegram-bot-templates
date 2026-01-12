from telegrinder import Message, Dispatch
from telegrinder.rules import Text

dp = Dispatch()

@dp.message(Text("ping"))
async def ping_handler(message: Message):
    await message.answer("🏓 Pong")
