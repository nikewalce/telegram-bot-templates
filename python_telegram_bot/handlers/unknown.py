from telegram.ext import ContextTypes
from telegram import Update

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Если неизвестная команда
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
