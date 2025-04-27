from telegram import Update
from telegram.ext import ContextTypes

from news.scraping import get_news

from db.mongo_client import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user_id= user.id, name= user.first_name)
    await update.message.reply_text(
        f"Fala, {user.first_name}! Bem-vindo ao universo FURIA! Use /news para ver as notícias mais brabas do time."
    )

async def unrecognized_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Infelizmente não temos essa funcionalidade ainda... Mas teste um dos nossos campos:\n/news - Notícias mais recentes da FURIA."
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news_list = get_news("furia cs")
    for idx, news in enumerate(news_list, 1):
        message = f"{idx}. {news['title']}\n{news['snippet']}\n{news['link']}"
        await update.message.reply_text(message)
