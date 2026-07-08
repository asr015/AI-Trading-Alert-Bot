from nifty import get_nifty_data
from market_status import get_market_status
from telegram_bot import send_message

data = get_nifty_data()
market_status = get_market_status()

message = f"""
━━━━━━━━━━━━━━━━━━
📊 TradingASR AI

📈 NIFTY 50 : {data['price']}
📉 Change : {data['change']} ({data['change_pct']}%)

{market_status}

🕒 {data['time']}

🤖 Bot Status : Active ✅
━━━━━━━━━━━━━━━━━━
"""

send_message(message)
