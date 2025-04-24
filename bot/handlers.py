from telegram.ext import CommandHandler
from bot.commands import start

def register_handlers(application):
    application.add_handler(CommandHandler("start", start))
