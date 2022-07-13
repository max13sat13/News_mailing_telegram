
#кнопка связь с разработчиком
#возможно словосочетания


import time
import asyncio
from pars import ParserTelegramm
from handlers import*
from task import *
from delete import *
from help import *






loop = asyncio.get_event_loop()
loop.create_task(task())



def polling():
    executor.start_polling(dp)

loop = asyncio.get_event_loop()
loop.create_task(polling())






