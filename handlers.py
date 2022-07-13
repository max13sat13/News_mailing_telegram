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
from help import*

@dp.message_handler(Text(equals="*"), state='*')
async def menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["добавить канал", "удалить канал", "нужна помощь"]
    keyboard.add(*buttons)
    await message.answer('меню', reply_markup=keyboard)

def get_title():
    global users_data
    res = req.get(link)
    html = BeautifulSoup(res.text, 'html.parser')
    channels = html.find_all("title")
    global title_channel
    title_channel = ""
    for channel in channels:
        s = str(channel).strip("</title>").split(' – Telegram')
        title_channel = s[0]
        print(title_channel)



@dp.message_handler(commands=['start'], state='*')
async def enter_hello(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["добавить канал", "удалить канал", "нужна помощь"]
    keyboard.add(*buttons)
    await message.answer('──────▄██▌█▐██▄──────\n'
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








@dp.message_handler(Text(equals="добавить канал"), state='*')
async def enter_hello(message: types.Message):
    await message.answer('Введите ссылку на телеграмм канал, '
                         'посты которого вы хотите фильтровать.\n'
                         'Пример ссылки: t.me/shiprazbor или @shiprazbor')
    global file_data_id
    file_data_id = 'users_data.json'
    await CellarImport.hello.set()


@dp.message_handler(state=CellarImport.hello)
async def enter_text(message: types.Message, state: FSMContext):
    global link
    link = message.text

    new_link = re.split(r'[/@]', link)
    print(new_link)
    link = 'https://t.me/s/' + new_link[-1]

    try:
        get_title()
        if title_channel == "Telegram Messenger":
            await message.answer('Битая какая-то ссылка, попробуй другую.')
        elif title_channel:
            await message.answer('Канал ' + '"' + title_channel + '"' + ' был добавлен.')
            answer = message.text
            await state.update_data(answer1=answer)
            await message.answer('Введи слова или словосочетания по которым бот будет искать новости.\n'
                                 'Чтобы ввести несколько слов или словосочетаний, разделите их запятой.\n\n'
                                 'Пример ввода:\nштурвал, нейтронный ускоритель, заднее крыло, вонючка ёлочка')

            await CellarImport.text_tg.set()
        else: await message.answer("канал не найден, попробуйте ещё раз")
    except:
        await message.answer("Бррр, это не телеграмм-канал, это что-то другое.\n"
                             "Введи заново.")





@dp.message_handler(state=CellarImport.text_tg)
async def enter_words(message: types.Message, state: FSMContext):
    await CellarImport.words.set()
    answer = message.text
    morph = pymorphy2.MorphAnalyzer()
    global words
    words = message.text



    words = morph.parse(words)[0].normal_form
    words = words.lower().split(',')
    format_words = []
    for word in words:
        format_words.append(morph.parse(word)[0].normal_form)
    words = format_words

    await state.update_data(answer2=answer)
    await message.answer('Список слов сохранен.')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["содержат введенные слова", "не содержат введенные слова"]
    keyboard.add(*buttons)
    await message.answer("Фильтровать посты можно двумя способами:\n"
                         "-присылать посты которые содержат введенные слова\n"
                         "-присылать посты которые НЕ содержат введённые слова\n", reply_markup=keyboard)
    await CellarImport.words.set()
    await state.reset_state()


def record(): 
    get_title()
    users_data = {}
    current_data = {}
    current_data[current_id] =  {link : [words, choose, title_channel]}
    try:
        with open(file_data_id) as file_object:
            users_data = json.load(file_object)
    except:
        with open(file_data_id, 'w') as file_object:
            json.dump(current_data, file_object)
    else:
        if str(current_id) in users_data.keys():

            users_data[str(current_id)][link] = [words, choose, title_channel]
            with open(file_data_id, 'w') as file_object:
                json.dump(users_data, file_object)
        else:
            users_data[current_id] = {link : [words, choose, title_channel]}
            with open(file_data_id, 'w') as file_object:
                json.dump(users_data, file_object)

	
@dp.message_handler(Text(equals="содержат введенные слова"))
async def with_puree(message: types.Message):
    global choose
    choose = True
    global current_id
    current_id = message.from_user.id
    record()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["добавить канал", "удалить канал", "нужна помощь"]
    keyboard.add(*buttons)
    await message.answer("Фильтрация настроена.\nЕсли необходимо поменять настройки, "
                         "добавьте этот канал заново.\n"
                         'Чтобы прекратить рассылку этого канала, нажмите "Удалить канал"', reply_markup=keyboard)
    


@dp.message_handler(lambda message: message.text == "не содержат введенные слова")
async def without_puree(message: types.Message):
    global choose
    choose = False
    global current_id
    current_id = message.from_user.id
    record()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["добавить канал", "удалить канал", "нужна помощь"]
    keyboard.add(*buttons)
    await message.answer("Фильтрация настроена.\nЕсли необходимо поменять настройки "
                         "добавьте этот канал заново.\n"
                         'Чтобы прекратить рассылку этого канала, нажмите "Удалить канал"', reply_markup=keyboard)

