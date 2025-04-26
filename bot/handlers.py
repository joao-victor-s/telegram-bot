from telegram.ext import CommandHandler, MessageHandler, filters
from bot.commands import start, news

def register_handlers(application):
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
        application.add_handler(CommandHandler("news", news))

