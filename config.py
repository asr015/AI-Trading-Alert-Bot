# ==========================================
# TradingASR AI Pro v2.0
# File : config.py
# ==========================================

import os

# ==========================
# Telegram Secrets
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==========================
# Scanner Settings
# ==========================

TIMEFRAME = "1d"
PERIOD = "6mo"

# ---------- Bullish ----------

EMA_BULLISH = 30
EMA200_BULLISH = 20
RSI_BULLISH = 30
MACD_BULLISH = 20
VWAP_BULLISH = 20
CANDLE_BULLISH = 20
VOLUME_BULLISH = 20
RVOL_BULLISH = 20
EMA_RISING = 20
MOMENTUM = 40

# ---------- Bearish ----------

EMA_BEARISH = -30
EMA200_BEARISH = -20
RSI_BEARISH = -30
MACD_BEARISH = -20
VWAP_BEARISH = -20
CANDLE_BEARISH = -20
SELLING = -20
EMA_FALLING = -20
BEARISH_MOMENTUM = -40

# ---------- Smart Money ----------

SMART_ENTRY = 50
SMART_EXIT = -50

# ---------- Liquidity ----------

LIQUIDITY = 30

# ---------- Structure ----------

BOS = 30
CHOCH = -30

# ---------- Order Block ----------

ORDER_BLOCK = 30

# ---------- Fair Value Gap ----------

FVG = 40
FVG_HOLD = 20

# ---------- News ----------

POSITIVE_NEWS = 20
NEGATIVE_NEWS = -20

# ---------- Market Bias ----------

BULLISH_BIAS = 20
BEARISH_BIAS = -20

# ---------- Option Chain ----------

PCR_BULLISH = 20
PCR_BEARISH = -20

# ---------- High Probability ----------

BUY_SCORE = 180
SELL_SCORE = -180

STRONG_BUY = 250
STRONG_SELL = -250

# ---------- Risk Reward ----------

RR1 = 2
RR2 = 3
