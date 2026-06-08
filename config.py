import os
from dotenv import load_dotenv

load_dotenv()

# Bot token for Crypto Signal Bot
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8632515297:AAHKSbl6Y7rTFOjnIT5UkQvTJ16fEdv3Vag")

# These will be taken from Render environment variables
# Set them to the SAME values as your first bot
VIP_CHANNEL_ID = int(os.getenv("VIP_CHANNEL_ID"))
OWNER_ID = int(os.getenv("OWNER_ID"))
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "sergio_newmann")

PLANS = {
    "1week": {"name": "1 Week", "price": 49, "days": 7, "original": 100},
    "3months": {"name": "3 Months", "price": 149, "days": 90, "original": 300},
    "lifetime": {"name": "Lifetime", "price": 249, "days": None, "original": 1000}
}

PAYMENT_METHODS = {
    "btc": {"name": "Bitcoin (BTC)", "symbol": "₿"},
    "usdt": {"name": "USDT (TRC20)", "symbol": "💲"},
    "ltc": {"name": "LiteCoin (LTC)", "symbol": "Ł"},
    "doge": {"name": "Dogecoin (DOGE)", "symbol": "Ð"}
}

WALLET_ADDRESSES = {
    "btc": "3KXxcezpun9AJbNSg88PmD1HTH5s7inRXx",
    "usdt": "TWpr3drUQPBCLpHsbmHHsFwPwqM4X1PZEY",
    "ltc": "MPyWXR8WGNZS9gx4D1WFqoUtF4KSGczJMv",
    "doge": "DDxz1EUymydsBs2VC5ipNVNUSFkAS8DpEE"
}