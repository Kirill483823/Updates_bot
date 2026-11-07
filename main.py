from aiogram import Bot, Dispatcher
import asyncio
from Routers.Start_Bot import start_router
from Routers.Main_work import main_work_router

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(main_work_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())