from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def inline_simple(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Это минимальный пример inline-кнопок
    Пользователь пишет /start -> Бот показывает кнопки -> Пользователь нажимает кнопку ->
    -> Бот один раз реагирует и всё -> Без состояний, без логики диалога
    """
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Нажатие кнопки
    query.data → это callback_data
    Бот редактирует сообщение
    """
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")
