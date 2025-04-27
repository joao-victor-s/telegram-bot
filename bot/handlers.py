from telegram.ext import CommandHandler, MessageHandler, filters
from bot.commands import unrecognized_command, start, news

def register_handlers(application):
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unrecognized_command))
        application.add_handler(CommandHandler("news", news))

