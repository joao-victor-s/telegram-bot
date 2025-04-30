from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from news.scraping import get_news
from matches.get_matches import get_furia_matches
from db.mongo_client import add_user

def build_main_menu():
    keyboard = [
        [InlineKeyboardButton("📰 Ver notícias", callback_data="news")],
        [InlineKeyboardButton("📅 Ver últimas partidas", callback_data="matches")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_send_method(update: Update):
    if update.message:
        return update.message.reply_text
    elif update.callback_query:
        return update.callback_query.message.reply_text
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user_id= user.id, name= user.first_name)
    add_user(user.id, user.first_name)
    await update.message.reply_text(
        f"Fala, {user.first_name}! Bem-vindo ao universo FURIA! 👊",
        reply_markup=build_main_menu()
     )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send = get_send_method(update)
    if not send:
        return

    news_list = get_news("furia cs")
    for idx, item in enumerate(news_list, 1):
        message = (
            f"*{idx}. {item['title']}*\n"
            f"{item['snippet']}\n"
            f"[🔗 Acessar notícia]({item['link']})"
        )
        await send(message, parse_mode="Markdown")

async def matchs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send = get_send_method(update)
    if not send:
        return

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

    await send(message_block.strip(), parse_mode="Markdown")


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "news":
        await news(update, context)
    elif query.data == "matches":
        await matchs(update, context)
