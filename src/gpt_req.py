from g4f import AsyncClient
from aiogram import types
from aiogram.enums.parse_mode import ParseMode

from text import *



async def text_request(msg: types.Message, model, promt, **premium):
    
    client = AsyncClient()
    
    try:
        
        response = await client.chat.completions.create(
            
        model=model,
        messages=[{"role" : "user", "content": promt}],
        web_search = False
            
        )
        answer = response.choices[0].message.content
        answer = answer.replace("**", "*")
        
        await msg.edit_text(answer, parse_mode=ParseMode.MARKDOWN_V2)
    
    except Exception as e:
        await msg.edit_text(tm_text_generation_error, parse_mode=ParseMode.MARKDOWN_V2)