import os
import requests
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

def get_prices():
    url = "https://api.tgju.org/v1/widget/latest"
    data = requests.get(url, timeout=10).json()["data"]

    dollar = data["price_dollar_rl"]["p"]
    gold = data["geram18"]["p"]
    coin = data["sekkeh"]["p"]

    return dollar, gold, coin


async def send_to_channel():
    try:
        d, g, c = get_prices()

        text = (
            "📊 قیمت لحظه‌ای بازار ایران\n\n"
            f"💵 دلار: {d}\n"
            f"🥇 طلا: {g}\n"
            f"🪙 سکه: {c}\n\n"
            "⏱ بروزرسانی: هر ۳۰ دقیقه"
        )

        await bot.send_message(chat_id=CHANNEL_ID, text=text)

    except Exception as e:
        print("Error:", e)


async def main():
    while True:
        await send_to_channel()
        await asyncio.sleep(1800)  # 30 minutes


if __name__ == "__main__":
    asyncio.run(main())
