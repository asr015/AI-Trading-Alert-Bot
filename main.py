
import os
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_message():
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(
        chat_id=CHAT_ID,
        text="Bot Working ✅\n\nGitHub → Telegram connection successful."
    )

if __name__ == "__main__":
    send_message()
