from aiogram.fsm.state import StatesGroup, State


class ChoosingBot(StatesGroup):
    TextGenModel = State()
    Gpt4 = State()
    Gpt4o = State()
    Gemini = State()
    Llama = State()
    Fastest = State()
    Pic = State()
    Mistral = State()
    
    
