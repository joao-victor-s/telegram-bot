# FURIA Telegram Bot

A Telegram bot that delivers the latest news and match updates about the FURIA Esports team, with support for inline keyboard interaction, web scraping, and containerized deployment.

---

## Features

- `/start` command with interactive inline keyboard menu
- `/news` command to fetch the latest FURIA news via web scraping
- `/matchs` command to display the most recent 5 FURIA matches
- Callback handling with button-based navigation
- Graceful fallback for unrecognized user messages
- Markdown-formatted messages for a better reading experience
- Dockerized infrastructure for easy deployment
- GitHub Actions CI for automated builds and validation

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/seu-usuario/furia-telegram-bot.git
cd furia-telegram-bot
```
### 2. Create a Telegram Bot

To enable the FURIA Telegram Bot to interact with users, you need to create a bot instance through Telegram. This is required to obtain a unique **Bot Token**, which allows your application to authenticate and communicate with the Telegram API.

Creating a bot is simple and manual — all steps are performed directly through the Telegram app using **BotFather**, an official Telegram bot designed to help users create and manage other bots.


#### 2.1 Open Telegram

Ensure that the **Telegram app** is installed on your device (desktop or mobile). You can download it from [telegram.org](https://telegram.org) if necessary.


#### 2.2 Start a chat with BotFather

1. Open Telegram and search for `@BotFather`.
2. Select the verified result and start a conversation.
3. Send the `/start` command to activate the bot interface.

BotFather will reply with a list of commands for bot management.



#### 2.3 Create your new bot

Then follow the guided steps:

- **Bot Name**: This is your bot’s display name (e.g., `FURIA News Bot`). It can contain spaces and will appear in the chat header.
- **Username**: Must be unique and end in `bot` (e.g., `furianews_bot`, `furiabotofficial`).
After completing the setup, BotFather will respond with a message that includes your

#### 2.4 Get your Bot Token
After completing the setup, BotFather will respond with a message that includes your **Bot Token**, which looks like this:
v123456789:AAH8cEiX9-EXAMPLE-TOKEN-Vv7xV8Fqe
> ⚠️ **Keep this token secure.** It provides full access to your bot and should never be shared publicly.

#### 2.5 Test your bot (optional)

You can now find and open your bot using the username you chose (e.g., https://t.me/furianews_bot) and click **Start**. If everything is configured correctly, your bot will respond to commands like `/start`, `/news`, and `/matchs` once deployed.


### 3. Set up environment variables
Create a .env file in the root directory:
```bash
BOT_TOKEN=your_telegram_bot_token
MONGO_URI=your_mongodb_uri
```
---
### Tech Stack
- Python 3
- python-telegram-bot
- Selenium + Chromium (for dynamic news scraping)
- BeautifulSoup4 + lxml (for parsing match data)
- Docker & Docker Compose
- GitHub Actions for CI

---
### Usage

| Command   | Description                                         |
|-----------|-----------------------------------------------------|
| `/start`  | Displays a menu with options to view news or matches |
| `/news`   | Sends the latest headlines about FURIA              |
| `/matchs` | Shows the last 5 FURIA matches                      |


