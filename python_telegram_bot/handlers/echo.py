from telegram.ext import ContextTypes
from telegram import Update

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Эхо(возвращает, что написали)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)