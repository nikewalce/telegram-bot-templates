from telegrinder import Telegrinder, API, Token
from telegrinder import Message
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TOKEN")

api = API(Token(TOKEN))
bot = Telegrinder(api)

@bot.on.message()
async def message_handler(message: Message):
    await message.answer(message.text.unwrap_or("Нет текста"))

bot.run_forever()