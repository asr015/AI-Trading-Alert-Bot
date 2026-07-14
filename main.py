# ==========================================
# TradingASR AI Pro v2.2
# File : main.py
# ==========================================

from logger import log
from telegram_bot import send_message
from watchlist_runner import run_watchlist
from market_summary import create_summary
from option_chain import analyze_option_chain

log("TradingASR AI Scanner Started")

try:
    results = run_watchlist()
    results = sorted(results, key=lambda x: abs(x.get("score", 0)), reverse=True)[:5]

    summary = create_summary(results)
    option = analyze_option_chain()

    message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro v2.2

📈 MARKET SUMMARY

Stocks Scanned : {summary['total']}

🟢 Bullish : {summary['bullish']}
🟡 Neutral : {summary['neutral']}
🔴 Bearish : {summary['bearish']}

━━━━━━━━━━━━━━━━━━

📊 OPTION CHAIN

PCR : {option.get('PCR','N/A')}
Call Writing : {option.get('CallWriting','N/A')}
Put Writing : {option.get('PutWriting','N/A')}

━━━━━━━━━━━━━━━━━━

🔥 HIGH PROBABILITY TRADES
"""

    medals = ["🥇","🥈","🥉","4️⃣","5️⃣"]

    if not results:
        message += "\n❌ No High Probability Trade Found Today\n━━━━━━━━━━━━━━━━━━\n"

    for i, stock in enumerate(results):
        score = stock.get("score",0)
        if score >= 170:
            trade = "🟢 STRONG BUY"
        elif score <= -170:
            trade = "🔴 STRONG SELL"
        else:
            trade = "🟡 WATCHLIST"

        reasons = "\n".join(stock.get("reasons",[])[:4])
        ai_reasons = "\n".join(stock.get("ai_reasons",[])[:2])

        message += f"""
{medals[i]} {stock.get('symbol','Unknown')}

{trade}

Score : {score}
Confidence : {stock.get('confidence','Low')}

🎯 Entry : {stock.get('entry','N/A')}
🛑 Stop Loss : {stock.get('sl','N/A')}
🎯 Target 1 : {stock.get('target1','N/A')}
🚀 Target 2 : {stock.get('target2','N/A')}

📌 Technical Reasons

{reasons}
"""
        if ai_reasons:
            message += f"""

🤖 AI Confirmation

{ai_reasons}
"""
        message += "\n━━━━━━━━━━━━━━━━━━\n"

    message += "\n🤖 TradingASR AI Pro v2.2"
    send_message(message)
    log("Scanner Completed")

except Exception as e:
    error = f"\n❌ Scanner Error\n\n{str(e)}\n"
    send_message(error)
    log(str(e))
    
