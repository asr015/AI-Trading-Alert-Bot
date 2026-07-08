import os
import requests
import yfinance as yf
from datetime import datetime

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Nifty 50 data
nifty = yf.Ticker("^NSEI")
data = nifty.history(period="2d")

last_price = round(data["Close"].iloc[-1], 2)
prev_close = round(data["Close"].iloc[-2], 2)

change = round(last_price - prev_close, 2)
change_pct = round((change / prev_close) * 100, 2)

status = "🟢 OPEN" if datetime.now().hour >= 9 and datetime.now().hour < 15 else "🔴 CLOSED"

message = f"""
📊 AI Market Update

📈 NIFTY 50 : {last_price}
📉 Change : {change} ({change_pct}%)

{status}

🤖 Bot Status : Active ✅
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
