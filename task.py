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



async def task():
	while True:
		file_chat_id = 'users_data.json'
		try:
			with open(file_chat_id) as file_object:
				users_data = json.load(file_object)
		except: users_data = {}
		for user_id, data in users_data.items():
			for link, words_choose in data.items():
				words = words_choose[0]					
				choose = words_choose[1]
				user_name = ParserTelegramm(link, words, choose, user_id)
				user_name.get_data()
				user_name.parser_text()
				user_name.uniq_message()
				start = user_name.output_telegram()
				if start:
					for message in start:
						await bot.send_message(user_id, message)

				else:
					await asyncio.sleep(2)
		await asyncio.sleep(2)
