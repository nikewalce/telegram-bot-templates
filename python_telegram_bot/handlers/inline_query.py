from telegram.ext import ContextTypes
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from html import escape #escape() защищает от HTML-инъекций
from telegram.constants import ParseMode

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    если пользователь вводит @имя_бота текст
    → бот предлагает варианты вставки текста:
    В ВЕРХНЕМ РЕГИСТРЕ
    Жирным
    Курсивом
    InlineQueryResultArticle() - один вариант ответа в inline-режиме
    """
    query = update.inline_query.query

    #Если пользователь просто написал @botusername — бот ничего не делает
    if not query:
        return

    #Создаются 3 варианта, которые пользователь может выбрать
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
            ),
        ),
    ]

    await update.inline_query.answer(results)
