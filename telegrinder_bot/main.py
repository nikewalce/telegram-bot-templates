from telegrinder import Telegrinder, API, Token

api = API(Token("5873982989:AAHQopiGJ17LQJ-GDxSu6pbA9whLaVBhCAA"))
bot = Telegrinder(api)

# Добавим импорт
from telegrinder import Message

@bot.on.message()
async def message_handler(message: Message):
    await message.answer(message.text.unwrap_or("Нет текста"))

bot.run_forever()