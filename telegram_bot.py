# ==========================================
# TradingASR AI Pro v4.0
# File : telegram_bot.py
# Part 1 / 5
# ==========================================

import requests

from config import BOT_TOKEN, CHAT_ID

TELEGRAM_URL = (
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
)


# ==========================================
# SEND MESSAGE
# ==========================================

def send_message(message):

    if not BOT_TOKEN or not CHAT_ID:

        print("Telegram configuration missing")

        return False

    try:

        payload = {

            "chat_id": CHAT_ID,

            "text": message,

            "parse_mode": "HTML",

            "disable_web_page_preview": True

        }

        response = requests.post(

            TELEGRAM_URL,

            json=payload,

            timeout=20

        )

        response.raise_for_status()

        return True

    except Exception as e:

        print(f"Telegram Error : {e}")

        return False
