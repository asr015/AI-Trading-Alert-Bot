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
        # ======================================
    # HIGH PROBABILITY TRADES
    # ======================================

    msg += "<b>🏆 TOP HIGH PROBABILITY TRADES</b>\n\n"

    if not trades:

        msg += "❌ No High Probability Trade Found\n"

    else:

        # Best trades first
        trades = sorted(

            trades,

            key=lambda x: abs(x.get("score", 0)),

            reverse=True

        )[:5]

        for trade in trades:

            msg += (
                f"<b>{trade.get('symbol','')}</b>\n"
            )

            msg += (
                f"{trade.get('verdict','WAIT')}\n"
            )

            msg += (
                f"⭐ {trade.get('setup','N/A')}\n"
            )

            msg += (
                f"AI Score : {trade.get('score',0)}\n"
            )

            msg += (
                f"Confidence : "
                f"{trade.get('confidence','0%')}\n\n"
            )

            msg += (
                f"Entry : {trade.get('entry','N/A')}\n"
            )

            msg += (
                f"SL : {trade.get('sl','N/A')}\n"
            )

            msg += (
                f"T1 : {trade.get('target1','N/A')}\n"
            )

            msg += (
                f"T2 : {trade.get('target2','N/A')}\n\n"
            )

            msg += "<b>Reasons</b>\n"

            reasons = trade.get("reasons", [])

            for reason in reasons[:8]:

                msg += f"• {reason}\n"

            msg += "\n"
                # ======================================
    # FOOTER
    # ======================================

    msg += (
        "<b>━━━━━━━━━━━━━━━━━━━━</b>\n"
    )

    msg += (
        "<b>TradingASR AI Pro v4.0</b>\n"
    )

    msg += (
        "Institutional AI Trading Assistant\n"
    )

    msg += (
        "⚠️ Educational Purpose Only\n"
    )

    # ======================================
    # TELEGRAM MESSAGE LIMIT
    # ======================================

    if len(msg) <= 4000:

        return [msg]

    messages = []

    current = ""

    for line in msg.split("\n"):

        if len(current) + len(line) + 1 > 4000:

            messages.append(current)

            current = ""

        current += line + "\n"

    if current:

        messages.append(current)

    return messages


# ==========================================
# SEND REPORT
# ==========================================

def send_report(summary, option_chain, index_data, trades):

    messages = build_message(

        summary,

        option_chain,

        index_data,

        trades

    )

    success = True

    for message in messages:

        if not send_message(message):

            success = False

    return success
    # ==========================================
# TELEGRAM RETRY ENGINE
# ==========================================

import time


def send_with_retry(message, retry=3):

    for attempt in range(retry):

        try:

            if send_message(message):
                return True

        except Exception as e:

            print(
                f"Retry {attempt+1}/{retry} : {e}"
            )

        time.sleep(2)

    return False


# ==========================================
# FILTER HIGH PROBABILITY TRADES
# ==========================================

def filter_high_probability(trades):

    filtered = []

    for trade in trades:

        score = trade.get("score", 0)

        confidence = trade.get("confidence", "0%")

        try:
            confidence_value = int(
                confidence.replace("%", "")
            )
        except Exception:
            confidence_value = 0

        setup = trade.get("setup", "")

        # Institutional Quality Filter
        if (

            abs(score) >= 250

            and confidence_value >= 90

            and (
                "⭐⭐⭐⭐" in setup
                or
                "⭐⭐⭐⭐⭐" in setup
            )

        ):

            filtered.append(trade)

    filtered.sort(

        key=lambda x: abs(x["score"]),

        reverse=True

    )

    return filtered[:5]


# ==========================================
# MAIN TELEGRAM FUNCTION
# ==========================================

def send_ai_report(

    summary,

    option_chain,

    index_data,

    trades

):

    trades = filter_high_probability(trades)

    messages = build_message(

        summary,

        option_chain,

        index_data,

        trades

    )

    success = True

    for message in messages:

        if not send_with_retry(message):

            success = False

    return success
