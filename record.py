import logging

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
from pars import ParserTelegramm
from fsm_config import*

#проверка github
def record(): 
    global users_data
    
    users_data = {}
    current_data = {}
    current_data[current_id] =  {link : {words : choose}}
    try:
        with open(file_data_id) as file_object:
            users_data = json.load(file_object)
    except:
        with open(file_data_id, 'w') as file_object:
            json.dump(current_data, file_object)
    else:
        if str(current_id) in users_data.keys():
            print("ок")
            users_data[str(current_id)][link] = {words : choose}
        else:
            users_data[current_id] = {link : {words : choose}}
            with open(file_data_id, 'w') as file_object:
                json.dump(users_data, file_object)
        print(users_data)
