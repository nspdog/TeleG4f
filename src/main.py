import asyncio

from aiogram import Bot, Dispatcher

from aiogram.enums.parse_mode import ParseMode

from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

import logging


from cfg import DataInfo
from handlers import router


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")




async def main():
    redis = Redis(host='localhost')
    bot = Bot(token = DataInfo.TOKEN)
    dp = Dispatcher(storage=RedisStorage(redis=redis))
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    finally:
        print("\nProgramm")