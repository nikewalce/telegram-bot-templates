from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

"""
Это настоящий интерактивная клавиатура с логикой переходов
Используется ConversationHandler

- кнопки меняются
- сообщение не отправляется заново, а редактируется
- бот помнит, на каком шаге диалога пользователь
"""

"""
Это этапы диалога
START_ROUTES — основной выбор
END_ROUTES — финальный шаг
"""
START_ROUTES, END_ROUTES = range(2)
"""
Callback data
Идентификаторы кнопок (что именно нажал пользователь)
"""
ONE, TWO, THREE, FOUR = range(4)


async def dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    /dialog
    Показывает первые кнопки 1 и 2
    Начинает диалог
    Возвращает состояние START_ROUTES
    """
    # Get user that sent /dialog and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)

    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Срабатывает при возврате к началу
    Не отправляет новое сообщение
    Редактирует старое сообщение
    Возвращает START_ROUTES
    """
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    await query.edit_message_text(text="Start handler, Choose a route", reply_markup=reply_markup)
    return START_ROUTES


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Пользователь нажал кнопку 1
    Показывает кнопки 3 и 4
    Остаётся в START_ROUTES
    """
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("3", callback_data=str(THREE)),
            InlineKeyboardButton("4", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="First CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return START_ROUTES


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Пользователь нажал кнопку 2
    Показывает кнопки 1 и 3
    Остаётся в START_ROUTES
    """
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Second CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return START_ROUTES


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Конечная точка диалога
    Спрашивает, начать ли сначала
    Переходит в END_ROUTES
    """
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Yes, let's do it again!", callback_data=str(ONE)),
            InlineKeyboardButton("Nah, I've had enough ...", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Third CallbackQueryHandler. Do want to start over?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return END_ROUTES


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Альтернативная ветка
    Показывает кнопки 2 и 3
    Возвращается в START_ROUTES
    """
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Fourth CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return START_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Закрывает разговор
    Возвращает ConversationHandler.END
    """
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END
