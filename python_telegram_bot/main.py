import logging
from telegram import Update
from telegram.ext import (ConversationHandler, CallbackQueryHandler,
                          ApplicationBuilder, CommandHandler,
                          MessageHandler, filters, InlineQueryHandler,
                          ShippingQueryHandler, PreCheckoutQueryHandler)
from python_telegram_bot.config import BOT_TOKEN
from python_telegram_bot.handlers.start import start
from python_telegram_bot.handlers.echo import echo
from python_telegram_bot.handlers.caps import caps, inline_caps
from python_telegram_bot.handlers.unknown import unknown
from python_telegram_bot.handlers.inline_query import inline_query
from python_telegram_bot.keyboadrs.inline_simple import inline_simple, button
from python_telegram_bot.keyboadrs.inline_logic_steps import (dialog, one, two, three, four,
                                                              start_over, end, START_ROUTES,
                                                              END_ROUTES, ONE, TWO, THREE, FOUR)
from python_telegram_bot.handlers.payment import (start_callback, start_with_shipping_callback,
                                                  start_without_shipping_callback,
                                                  shipping_callback, precheckout_callback,
                                                  successful_payment_callback)

#настройки logging модуля, чтобы знать, когда (и почему) что-то работает не так, как ожидалось
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    """
    ApplicationBuilder() - http://docs.python-telegram-bot.org/en/stable/telegram.ext.applicationbuilder.html#telegram-ext-applicationbuilder
    CommandHandler() - #https://docs.python-telegram-bot.org/en/stable/telegram.ext.commandhandler.html
    filters - https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html
    InlineQueryHandler() - https://docs.python-telegram-bot.org/en/stable/telegram.ext.inlinequeryhandler.html
    MessageHandler фильтр COMMAND для ответа на все команды, которые не были распознаны предыдущими обработчиками
    InlineQueryHandler() - обработка inline-запросов. Чтобы включить: в BotFather: /mybots -> выбираем бота -> Bot Settings -> Inline Mode -> Turn on
    ShippingQueryHandler() - Выбор и стоимость доставки, После ввода адреса
    PreCheckoutQueryHandler() - Разрешение списать деньги, Перед оплатой
    """
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    # вызывает inline простую клавиатуру
    inline_simple_keyboard = CommandHandler("inline_simple", inline_simple)
    inline_simple_button = CallbackQueryHandler(button)
    #Оплата
    payment_handler = CommandHandler("payment", start_callback)
    shipping_handler = CommandHandler("shipping", start_with_shipping_callback)
    noshipping_handler = CommandHandler("noshipping", start_without_shipping_callback)
    shipping_callback_handler = ShippingQueryHandler(shipping_callback)
    precheckout_callback_handler = PreCheckoutQueryHandler(precheckout_callback)
    # если неизвестная команда
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(InlineQueryHandler(inline_query))
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)
    # вызывает inline простую клавиатуру
    application.add_handler(inline_simple_keyboard)
    application.add_handler(inline_simple_button)
    """
    ConversationHandler Определяет:
    с чего начинается диалог
    какие кнопки работают в каждом состоянии
    куда переходить дальше
    """
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("dialog", dialog)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
            ],
        },
        fallbacks=[CommandHandler("dialog", dialog)],
    )
    application.add_handler(conv_handler)

    #Оплата
    application.add_handler(payment_handler)
    application.add_handler(shipping_handler)
    application.add_handler(noshipping_handler)
    application.add_handler(shipping_callback_handler)
    application.add_handler(precheckout_callback_handler)
    application.add_handler(
        MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    # если неизвестная команда
    application.add_handler(unknown_handler)

    #запускает бота до тех пор, пока не нажать CTRL+C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
