"""
Сборка диспетчеров
- это контейнер логики
- позволяет легко масштабировать проект
- порядок загрузки = порядок обработки
"""

from telegrinder import Dispatch
from telegrinder_bot.handlers import start, echo, api_examples, callbacks, menu, handle_keyboard, ping

def build_dispatch() -> Dispatch:
    dp = Dispatch()
    # загружаем диспетчеры из модулей
    dp.load(start.dp)
    #dp.load(api_examples.dp)
    dp.load(menu.dp)
    dp.load(handle_keyboard.dp)
    dp.load(callbacks.dp)
    dp.load(ping.dp)
    dp.load(echo.dp)  # fallback — ВСЕГДА ПОСЛЕДНИМ
    return dp
