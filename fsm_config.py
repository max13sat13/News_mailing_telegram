import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = ''

bot = Bot(token=API_TOKEN)

class CellarImport(StatesGroup):
    hello = State()
    text_tg = State()
    words = State()
    delete = State()

    
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
