from logger import log
from telegram_bot import send_message
from watchlist_runner import run_watchlist

log("TradingASR AI Scanner Started")

try:

    results = run_watchlist()

    message = """
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Scanner

"""

    medals = ["🥇", "🥈", "🥉"]

    for i, stock in enumerate(results):

        message += f"""
{medals[i]} {stock['symbol']}

Score : {stock['score']}/100

{stock['signal']}

Confidence : {stock['confidence']}

"""

    message += """
━━━━━━━━━━━━━━━━━━
🤖 TradingASR AI Pro
"""

    send_message(message)

    log("Scanner Completed")

except Exception as e:

    send_message(f"❌ Scanner Error\n\n{str(e)}")

    log(str(e))
