# ==========================================
# TradingASR AI Pro v2.0
# File : telegram_bot.py
# ==========================================

import requests

from config import BOT_TOKEN, CHAT_ID


def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:

        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=15
        )

        response.raise_for_status()

        return True

    except requests.RequestException as e:

        print(f"Telegram Error: {e}")

        return False
