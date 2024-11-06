from gpt_req import get_responce
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from gpt_req import get_responce
from cfg import TOKEN
from aiogram.types import FSInputFile

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logger = logging.getLogger(__name__)

#logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()


 
@dp.message()
async def send_answer_request(message: types.Message):
    print(message.text)    
    await message.answer("Идет формирование ответа")
    await message.answer(get_responce(message))
    

@dp.message(Command("start"))
async def star_comma(message: types.Message):
    await message.answer("bububiba?")
    


async def main():
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())