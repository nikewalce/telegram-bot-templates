from telegrinder import Dispatch, Message
from telegrinder.rules import Command

dp = Dispatch()

@dp.message(Command("start"))
async def start_handler(message: Message):
    """
        answer — удобная обёртка над send_message
        Он вызывает метод send_message в Telegram с уже указанным chat_id
    """
    await message.answer("👋 Hi! I'm telegrinder bot.")
