from nifty import get_nifty_data
from telegram_bot import send_message

data = get_nifty_data()

message = f"""
📊 TradingASR AI

📈 NIFTY 50 : {data['price']}
📉 Change : {data['change']} ({data['change_pct']}%)

{data['status']}

🕒 {data['time']}

🤖 Bot Status : Active ✅
"""

send_message(message)
