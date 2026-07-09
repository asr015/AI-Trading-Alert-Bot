from logger import log
from telegram_bot import send_message
from watchlist_runner import run_watchlist
from market_summary import create_summary
from option_chain import analyze_option_chain


log("TradingASR AI Scanner Started")

try:

    results = run_watchlist()

    summary = create_summary(results)

    option = analyze_option_chain()

    message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro

📈 MARKET SUMMARY

Stocks Scanned : {summary['total']}

🟢 Bullish : {summary['bullish']}
🟡 Neutral : {summary['neutral']}
🔴 Bearish : {summary['bearish']}

📊 OPTION CHAIN

PCR : {option['PCR']}

Call Writing : {option['CallWriting']}

Put Writing : {option['PutWriting']}

🔥 TOP MOMENTUM STOCKS

"""

    medals = ["🥇", "🥈", "🥉"]

    for i, stock in enumerate(results):

        reasons = "\n".join(stock["reasons"][:3])

        message += f"""
{medals[i]} {stock['symbol']}

Score : {stock['score']}/270

{stock['verdict']}

Confidence : {stock['confidence']}

{reasons}

"""

    message += """
━━━━━━━━━━━━━━━━━━
🤖 TradingASR AI Pro v1.0
"""

    send_message(message)

    log("Scanner Completed")

except Exception as e:

    send_message(
        f"❌ Scanner Error\n\n{str(e)}"
    )

    log(str(e))
