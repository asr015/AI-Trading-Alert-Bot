# ==========================================
# TradingASR AI Pro v2.3
# File : telegram_bot.py
# ==========================================

import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }

    try:

        response = requests.post(
            url,
            data=payload,
            timeout=20
        )

        # Debug Output
        print("Status Code :", response.status_code)
        print("Telegram Response :", response.text)

        response.raise_for_status()

        result = response.json()

        if not result.get("ok", False):
            print("Telegram API Error :", result)
            return False

        print("Telegram Message Sent Successfully")
        return True

    except requests.exceptions.Timeout:

        print("Telegram Error : Request Timed Out")
        return False

    except requests.exceptions.ConnectionError:

        print("Telegram Error : Connection Failed")
        return False

    except requests.RequestException as e:

        print(f"Telegram Error : {e}")
        return False

    except Exception as e:

        print(f"Unexpected Error : {e}")
        return False
