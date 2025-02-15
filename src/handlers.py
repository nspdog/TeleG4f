from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.enums.parse_mode import ParseMode

import kb
from text import *
from states import ChoosingBot
from gpt_req import *


router = Router()


@router.message(Command('start'))
async def start_message(msg: types.Message):
    await msg.answer(tm_start_message, reply_markup=kb.choosing_option_kb())
    await msg.answer("*meeeow*", parse_mode=ParseMode.MARKDOWN_V2)

@router.callback_query(F.data == "menu")    
@router.callback_query(F.data == "back")    
async def back(call: types.CallbackQuery):
    await call.message.answer(tm_menu, reply_markup=kb.choosing_option_kb())
    
@router.callback_query(F.data == "ch_text")
async def set_state_gpt(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(tm_choosing_gpt, reply_markup=kb.choosing_gpt_kb())
    
    
@router.callback_query(F.data == "ch_pic")
async def set_state_gpt(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text()

@router.callback_query(F.data == "ch_code")
async def set_state_gpt(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(tm_choosing_code)
    await state.set_state(ChoosingBot.Mistral)
    
@router.callback_query(StateFilter("ChoosingBot:Mistral"))
async def generating_code(msg: types.Message, state: FSMContext):
    promt = msg.text
    msg = await msg.answer(tm_text_generation)
    await text_request(msg = msg, model = "mixtral-8x7b", promt=promt)
    

@router.callback_query(F.data == "call_gpt4")
@router.callback_query(F.data == "call_gpt4o")
@router.callback_query(F.data == "call_gemini")
@router.callback_query(F.data == "call_llama")
@router.callback_query(F.data == "fastest")
async def set_state_gpt(call: types.CallbackQuery, state: FSMContext):
    
    await state.set_state(ChoosingBot.TextGenModel)
    await call.message.edit_text(tm_ask_text)
    
    
    match F.data:
        
        case "call_gpt4":
            await state.set_data("gpt-4")
            
        case "call_gpt4o":
            await state.set_data(TextGenModel = "gpt-4o")
            
        case "call_gemini":
            await state.set_data(mode = "gemini")
            
        case "call_llama":
            await state.set_data(mode = "llama-3.3-70b")   
            
        case "fastest":
            await state.set_data(mode = "")
            
            

@router.callback_query(F.data == "null")
@router.message(StateFilter("ChoosingBot:TextGenModel"))
async def generating_text(msg: types.Message, state: FSMContext):
    model = await state.get_data()
    promt = msg.text
    
    msg = await msg.answer(tm_text_generation, parse_mode= ParseMode.MARKDOWN)
    await (text_request(msg, model= model, promt=promt))


@router.message(Command("help"))
async def help_message(msg: types.Message, state: FSMContext):
    await state.clear()
    await msg.answer(tm_help)
    

@router.message(Command("Menu"))
async def menu_command(msg: types.Message, state: FSMContext):
    await state.clear()
    await msg.answer(tm_menu, reply_markup=kb.menu_kb)
    
