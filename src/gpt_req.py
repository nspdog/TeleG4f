from g4f.client import Client
from cfg import *
import asyncio
from aiogram import types

def get_responce(message: types.Message):
    client = Client()
    responce_data = message.text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{responce_data}"}],

    )
    return str((f"{response.choices[0].message.content}"))

