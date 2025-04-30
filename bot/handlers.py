from telegram.ext import CommandHandler, MessageHandler, filters
from bot.commands import unrecognized_command, start, news, matchs

def register_handlers(application):
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unrecognized_command))
        application.add_handler(CommandHandler("news", news))
        application.add_handler(CommandHandler("matchs", matchs))


