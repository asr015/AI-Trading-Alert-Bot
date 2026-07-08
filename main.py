from option_chain import get_option_chain
from telegram_bot import send_message

try:
    data = get_option_chain()

    records = len(data["records"]["data"])

    message = f"""
✅ NSE Option Chain Connected

Total Strike Records : {records}

TradingASR AI Ready 🚀
"""

except Exception as e:

    message = f"""
❌ Option Chain Error

{str(e)}
"""

send_message(message)
