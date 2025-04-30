from telegram import Update
from telegram.ext import ContextTypes

from news.scraping import get_news
from matches.get_matches import get_furia_matches

from db.mongo_client import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user_id= user.id, name= user.first_name)
    await update.message.reply_text(
        f"Fala, {user.first_name}! Bem-vindo ao universo FURIA! Use /news para ver as notícias mais brabas do time."
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news_list = get_news("furia cs")
    for idx, news in enumerate(news_list, 1):
        message = f"{idx}. {news['title']}\n{news['snippet']}\n{news['link']}"
        await update.message.reply_text(message)

async def matchs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    furia_matches = get_furia_matches()
    message_block = ""

    for i, match in enumerate(furia_matches, 1):
        message_block += (
            f"🎯 *Partida {i}*\n"
            f"📅 {match['date']}\n"
            f"🏆 {match['tournament']} ({match['tier']} | {match['type']})\n"
            f"🆚 *{match['team_1']}* vs *{match['team_2']}*\n"
            f"🔢 *Placar:* {match['score']}\n\n"
        )

    await update.message.reply_text(message_block.strip(), parse_mode="Markdown")
