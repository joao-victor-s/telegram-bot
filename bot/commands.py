from telegram import Update
from telegram.ext import ContextTypes

from db.mongo_client import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user_id= user.id, name= user.first_name)
    await update.message.reply_text(
        f"Fala, {user.first_name}! Bem-vindo ao universo FURIA! Use /stats para ver os números mais brabos do time."
    )
