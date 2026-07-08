from logger import log
from nifty import get_nifty_data
from market_status import get_market_status
from telegram_bot import send_message

log("TradingASR AI Started")

try:
    data = get_nifty_data()
    market_status = get_market_status()

    message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI Pro

📈 NIFTY 50 : {data['price']}
📉 Change : {data['change']} ({data['change_pct']}%)

{market_status}

🕒 {data['time']}

🤖 Bot Status : Active ✅

Version : v0.5
━━━━━━━━━━━━━━━━━━
"""

    send_message(message)

    log("Telegram Alert Sent Successfully")

except Exception as e:

    log(f"ERROR : {str(e)}")

    send_message(f"""
❌ TradingASR AI Error

{str(e)}
""")
