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
        # ==========================================
# MESSAGE BUILDER
# ==========================================

def build_message(summary, option_chain, index_data, trades):

    msg = ""

    # ======================================
    # HEADER
    # ======================================

    msg += "<b>📊 TradingASR AI Pro v4.0</b>\n\n"

    # ======================================
    # MARKET SUMMARY
    # ======================================

    msg += "<b>📈 MARKET SUMMARY</b>\n"

    msg += (
        f"Stocks Scanned : "
        f"{summary.get('scanned', 0)}\n"
    )

    msg += (
        f"🟢 Bullish : "
        f"{summary.get('bullish', 0)}\n"
    )

    msg += (
        f"🟡 Neutral : "
        f"{summary.get('neutral', 0)}\n"
    )

    msg += (
        f"🔴 Bearish : "
        f"{summary.get('bearish', 0)}\n\n"
    )

    # ======================================
    # INDEX SIGNALS
    # ======================================

    msg += "<b>📊 INDEX SIGNALS</b>\n"

    for name, data in index_data.items():

        msg += (
            f"{name} : "
            f"{data.get('signal','WAIT')} "
            f"({data.get('confidence','0%')})\n"
        )

    msg += "\n"

    # ======================================
    # OPTION CHAIN
    # ======================================

    msg += "<b>📊 OPTION CHAIN</b>\n"

    msg += (
        f"PCR : "
        f"{option_chain.get('PCR','N/A')}\n"
    )

    msg += (
        f"Call Writing : "
        f"{option_chain.get('CallWriting','N/A')}\n"
    )

    msg += (
        f"Put Writing : "
        f"{option_chain.get('PutWriting','N/A')}\n"
    )

    msg += (
        f"Max Pain : "
        f"{option_chain.get('MaxPain','N/A')}\n\n"
    )
