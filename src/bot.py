from cfg import TOKEN
import g4f
from g4f import AsyncClient
from googletrans import Translator


import logging
import asyncio

from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext



logging.basicConfig(level=logging.INFO)




bot = Bot(TOKEN)
dp = Dispatcher()
router = Router()

class ChoosingBot(StatesGroup):
    Gpt = State()
    Img = State()
    


@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("Вас приветствует телеграм бот с ChatGpt.\nЧтобы войти в режим генерации текста введите /gpt\nЧтобы перейти в режим генерации изображений введите /img")

@dp.message(Command('gpt'))
async def set_state_gpt(message: types.Message, state: FSMContext):
    await message.answer("Вы вошли в режим генерации текста, введите свой запрос и ChatGPT 4 на него ответит")
    await state.set_state(ChoosingBot.Gpt)
    
@dp.message(Command('img'))
async def set_state_gpt(message: types.Message, state: FSMContext):
    await message.answer("Вы вошли в режим генерации изображений, введите свой промпт и flux его сгенерирует")
    await state.set_state(ChoosingBot.Img)

#ChatGPT

@dp.message(StateFilter("ChoosingBot:Gpt"))
async def send_answer_request(message: types.Message):
    user_id = message.from_user.id
    user_input = message.text
    
    print(user_input)    
    msg = await message.answer("Идет формирование ответа")

    try:    
        client = AsyncClient()
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}],
            web_search = False
            
        )
        
        
        await msg.edit_text(response.choices[0].message.content, parse_mode='Markdown')    
    
    except Exception as e:
        print("Error: ", e)
        chat_gpt_response = "Произошла ошибка в генерации текста..."
    
    
    #await msg.edit_text(chat_gpt_response, parse_mode='Markdown')


#image
@dp.message(StateFilter("ChoosingBot:Img"))
async def send_image(message: types.Message):
    user_input = await (translate_text(str(message.text)))
    msg = await message.answer("Подождите, идет генерация изображения...")
    try:
        client = AsyncClient()
        response = await client.images.generate(
            prompt=user_input,
            model="flux",
            
            response_format="url"
    )
        await msg.edit_text(f"Ссылка на ваше изображение:\n{response.data[0].url}")
    except Exception as e:
        print("Error in generating image: ", e)
        await msg.edit_text("В генерации изображения произошла ошибка...")
        
 
 
async def translate_text(data: str):
    async with Translator() as translator:
        result = await translator.translate(data, dest='en', src='ru')
        return (result.text)



async def main():
    
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
