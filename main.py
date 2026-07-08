from logger import log
from telegram_bot import send_message
from signal_engine import generate_signal
from data_manager import get_market_data

log("TradingASR AI Started")

try:

    market = get_market_data()

    score = 85
    signal = generate_signal(score)

    message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro

📈 NIFTY : {market['nifty']['price']}

📉 Change : {market['nifty']['change']} ({market['nifty']['change_pct']}%)

{market['market_status']}

🧠 AI Signal : {signal['signal']}

🎯 Confidence : {signal['confidence']}

🕒 {market['nifty']['time']}

🤖 Bot Status : Active

━━━━━━━━━━━━━━━━━━
"""

    send_message(message)

    log("Telegram Message Sent")

except Exception as e:

    send_message(f"❌ ERROR\n\n{str(e)}")

    log(str(e))
