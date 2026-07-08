from logger import log
from nifty import get_nifty_data
from market_status import get_market_status
from telegram_bot import send_message
from signal_engine import generate_signal

log("TradingASR AI Started")

try:
    # Market Data
    data = get_nifty_data()
    market_status = get_market_status()

    # Temporary AI Signal
    # बाद में यह scanner और option chain से score लेगा
    score = 85
    signal = generate_signal(score)

    message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro

📈 NIFTY 50 : {data['price']}
📉 Change : {data['change']} ({data['change_pct']}%)

{market_status}

🧠 AI Signal : {signal['signal']}
🎯 Confidence : {signal['confidence']}

🕒 {data['time']}

🤖 Bot Status : Active ✅
Version : v0.6
━━━━━━━━━━━━━━━━━━
"""

    send_message(message)

    log("Telegram Alert Sent Successfully")

except Exception as e:

    error_message = f"""
❌ TradingASR AI Error

{str(e)}
"""

    send_message(error_message)

    log(f"ERROR: {str(e)}")
