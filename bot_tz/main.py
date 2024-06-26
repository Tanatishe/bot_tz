from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
import logging
from app.handlers import router



load_dotenv()

bot = Bot(token=f"{os.getenv('TOKEN')}")
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('BOT OFF')


