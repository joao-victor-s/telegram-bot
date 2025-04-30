from telegram.ext import CommandHandler, MessageHandler, filters, CallbackQueryHandler
from bot.commands import start, news, matchs, button_handler

def register_handlers(application):
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
        application.add_handler(CommandHandler("news", news))
        application.add_handler(CommandHandler("matchs", matchs))

        application.add_handler(CallbackQueryHandler(button_handler))
