from telegrinder import Telegrinder, API, Token
from telegrinder_bot.config import BOT_TOKEN
from telegrinder_bot.dispatch import build_dispatch
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

api = API(Token(BOT_TOKEN))
bot = Telegrinder(api)

# загружаем корневой диспетчер
bot.on.load(build_dispatch())

#Запускает бота в асинхронном режиме, и будет получать и обрабатывать обновления в цикле
bot.run_forever()
