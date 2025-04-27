from telegram.ext import ApplicationBuilder

from dotenv import load_dotenv
import os

from bot.commands import start
from bot.handlers import register_handlers

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


app = ApplicationBuilder().token(BOT_TOKEN).build()
register_handlers(app)

if __name__ == '__main__':
    app.run_polling()
