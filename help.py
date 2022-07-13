import logging
from bs4 import BeautifulSoup
import requests as req
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
import json
import time
import asyncio
import re
import pymorphy2
import string
from pars import ParserTelegramm
from fsm_config import*
from delete import*
from handlers import*

@dp.message_handler(Text(equals="нужна помощь"), state='*')
async def enter_hello(message: types.Message, state: FSMContext):
    global msg
    msg = message
    buttons = [types.InlineKeyboardButton(text="инструкция", callback_data='manual'),
               types.InlineKeyboardButton(text="связь с разработчиком", url='https://t.me/maxhitchacker')]
    keyboard = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
    keyboard.add(*buttons)
    await message.answer("Выберете пункт", reply_markup=keyboard)
    await state.reset_state()

@dp.callback_query_handler(text="manual")
async def manual(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["добавить канал", "удалить канал", "нужна помощь"]
    keyboard.add(*buttons)
    await msg.answer('──────▄██▌█▐██▄──────\n'
                         '─────▐███▌█▐███▌─────\n'
                         '─────████▌█▐████─────\n'
                         '────▐▌█▀▀▀█▀▀▀█▐▌────\n'
                         '────█▐▓▄▄▄▓▄▄▄▓▌█────\n'
                         '───▐▌██▓▓║║║▓▓██▐▌───\n'
                         '───█▐█▌▓╩╩╩╩╩▓▐█▌█───\n'
                         '───▌█████████████▐───\n\n'
                         'Добро пожаловать на сторону фильтрованного контента.\n\n'
                         'Я Дартс Грейдер, буду фильтровать посты в телеграмме и отправлять вам.\n\n'
                         'Вы задаёте слова и словочетания - дальше по ним я отбираю новости.\n\n'
                         'Нажмите "Добавить канал" - чтобы начать.\n\n'
                         'Нажмите "Нужна помощь" - если что-то пошло не по плану', reply_markup=keyboard)
    #await call.message.edit_text(text="ок", reply_markup="")
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)