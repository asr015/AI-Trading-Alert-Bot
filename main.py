from logger import log
from telegram_bot import send_message
from watchlist_runner import run_watchlist
from market_summary import create_summary
from option_chain import analyze_option_chain

log("TradingASR AI Scanner Started")

try:

    # ===========================
    # Run Scanner
    # ===========================

    results = run_watchlist()

    summary = create_summary(results)

    option = analyze_option_chain()

    message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro v1.1

📈 MARKET SUMMARY

Stocks Scanned : {summary['total']}

🟢 Bullish : {summary['bullish']}
🟡 Neutral : {summary['neutral']}
🔴 Bearish : {summary['bearish']}

📊 OPTION CHAIN

PCR : {option['PCR']}

Call Writing : {option['CallWriting']}

Put Writing : {option['PutWriting']}

━━━━━━━━━━━━━━━━━━

🔥 HIGH PROBABILITY TRADES

"""

    medals = [
        "🥇",
        "🥈",
        "🥉",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",
        "8️⃣",
        "9️⃣",
        "🔟"
    ]
        # ===========================
    # HIGH PROBABILITY TRADES
    # ===========================

    for i, stock in enumerate(results):

        medal = medals[i] if i < len(medals) else f"{i+1}."

        trade = "🟢 BUY" if stock["score"] >= 0 else "🔴 SELL"

        reasons = "\n".join(stock["reasons"][:4])

        message += f"""
{medal} {stock['symbol']}

{trade}

Score : {stock['score']}/270

Confidence : {stock['confidence']}

🎯 Entry : {stock['entry']}

🛑 Stop Loss : {stock['sl']}

🎯 Target 1 : {stock['target1']}

🚀 Target 2 : {stock['target2']}

Reason

{reasons}

━━━━━━━━━━━━━━━━━━
"""

    if len(results) == 0:

        message += """

❌ No High Probability Trade Found Today

"""

    message += """

🤖 TradingASR AI Pro v1.1

"""

    send_message(message)

    log("Scanner Completed")

except Exception as e:

    error = f"""

❌ Scanner Error

{str(e)}

"""

    send_message(error)

    log(str(e))
