from telegram.ext import ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    update объект, содержащий всю информацию и данные, поступающие из самого Telegram (например, сообщение, пользователь, отдавший команду и т. д.)
    context другой объект, содержащий информацию и данные о состоянии самой библиотеки (например Bot, Application, , и job_queueт. д.)
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="👋 I'm a python-telegram-bot!")
