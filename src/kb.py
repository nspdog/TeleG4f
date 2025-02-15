from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder 


def choosing_option_kb():
    
    choosing_option_buttons = [
        [InlineKeyboardButton(text="Генерация текста", callback_data="ch_text")],
        [InlineKeyboardButton(text="Генерация изображений", callback_data="ch_pic")],
        [InlineKeyboardButton(text="Генерация кода", callback_data="ch_code")]
        
        
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=choosing_option_buttons)

def choosing_gpt_kb():
    
    choosing_gpt_buttons = [
        [InlineKeyboardButton(text="ChatGPT-4", callback_data="call_gpt4")],
        [InlineKeyboardButton(text="ChatGPT-4o", callback_data="call_gpt4o")],
        [InlineKeyboardButton(text="Gemini", callback_data="call_gemini")],
        [InlineKeyboardButton(text="Llama", callback_data="call_llama")],
        [InlineKeyboardButton(text="Самый быстрый", callback_data="fastest")],
        [InlineKeyboardButton(text="Вернуться назад", callback_data="back")]
        
        
        
    ]  
    
    return InlineKeyboardMarkup(inline_keyboard=choosing_gpt_buttons)


def menu_kb():
    
    choosing_menu_buttons = [
        
    ]
    
    return(InlineKeyboardMarkup(inline_keyboard=choosing_menu_buttons))
    