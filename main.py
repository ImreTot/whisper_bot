import os

from dotenv import load_dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import router

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('BOT_TOKEN', 'BOT_TOKEN'))


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
