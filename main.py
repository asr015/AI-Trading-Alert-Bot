from logger import log
from option_chain_engine import analyze_option_chain
from telegram_bot import send_message
from watchlist_runner import run_watchlist
from market_summary import create_summary


log("TradingASR AI Scanner Started")

try:

    results = run_watchlist()

    summary = create_summary(results)
    option = analyze_option_chain()

    message = """
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro

📈 MARKET SUMMARY

Stocks Scanned : {total}

🟢 Bullish : {bullish}
🟡 Neutral : {neutral}
🔴 Bearish : {bearish}


🔥 TOP MOMENTUM STOCKS

""".format(**summary)


    medals = ["🥇", "🥈", "🥉"]

    for i, stock in enumerate(results):

        reasons = "\n".join(stock["reasons"][:3])

        message += f"""
{medals[i]} {stock['symbol']}
message += f"""

📊 OPTION CHAIN

PCR : {option['PCR']}

Call Writing : {option['CallWriting']}

Put Writing : {option['PutWriting']}

"""

Score : {stock['score']}/270

{stock['verdict']}

Confidence : {stock['confidence']}

{reasons}

"""


    message += """
━━━━━━━━━━━━━━━━━━
🤖 TradingASR AI Pro v0.9
"""


    send_message(message)

    log("Scanner Completed")


except Exception as e:

    send_message(
        f"❌ Scanner Error\n\n{str(e)}"
    )

    log(str(e))
