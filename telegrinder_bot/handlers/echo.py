from telegrinder import Dispatch, Message

dp = Dispatch()

@dp.message()
async def echo(message: Message):
    """fallback-обработчик — всегда последний"""
    await message.answer(
        message.text.unwrap_or("🤷 No text")
    )
