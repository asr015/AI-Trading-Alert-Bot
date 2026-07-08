from logger import log
from telegram_bot import send_message
from watchlist_runner import run_watchlist

log("TradingASR AI Scanner Started")

try:

    results = run_watchlist()

    message = "━━━━━━━━━━━━━━━━━━\n"
    message += "📊 TradingASR AI Scanner\n\n"

    medals = ["🥇", "🥈", "🥉"]

    for i, stock in enumerate(results):

        reasons = "\n".join(stock["reasons"][:3])

        message += (
            f"{medals[i]} {stock['symbol']}\n"
            f"Score : {stock['score']}/170\n"
            f"{stock['signal']}\n"
            f"Confidence : {stock['confidence']}\n\n"
            f"{reasons}\n\n"
        )

    message += "━━━━━━━━━━━━━━━━━━\n"
    message += "🤖 TradingASR AI Pro v0.8"

    send_message(message)

    log("Scanner Completed")

except Exception as e:

    send_message(f"❌ Scanner Error\n\n{str(e)}")

    log(str(e))
