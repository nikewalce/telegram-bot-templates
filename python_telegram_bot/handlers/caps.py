from telegram.ext import ContextTypes
from telegram import Update
from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /caps команду, которая будет принимать в качестве аргумента текст (например, /caps argument) и отвечать на него ЗАГЛАВНЫМИ буквами
    """
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)