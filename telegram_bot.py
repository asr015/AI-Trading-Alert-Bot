# ==========================================
# TradingASR AI Pro v2.2
# File : telegram_bot.py
# ==========================================

import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    try:

        response = requests.post(
            url,
            data=payload,
            timeout=15
        )

        response.raise_for_status()

        result = response.json()

        if not result.get("ok", False):
            print(f"Telegram API Error: {result}")
            return False

        return True

    except requests.exceptions.Timeout:

        print("Telegram Error: Request Timed Out")
        return False

    except requests.exceptions.ConnectionError:

        print("Telegram Error: Connection Failed")
        return False

    except requests.RequestException as e:

        print(f"Telegram Error: {e}")
        return False

    except Exception as e:

        print(f"Unexpected Telegram Error: {e}")
        return False
