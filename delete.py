
import json    

from fsm_config import*
from handlers import *
from help import *






def get_keyboard():
    # Генерация клавиатуры.
    buttons = []
    file_chat_id = 'users_data.json'
    try:
        with open(file_chat_id) as file_object:
            users_data = json.load(file_object)
            print(str(users_data) + 'user_data')
    except: users_data = {}
    else:
        for user_id, data in users_data.items():
            if str(this_id) == str(user_id):
                for link, all_data in data.items():
                    buttons.append(types.InlineKeyboardButton(text=all_data[2], callback_data=link))
    
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard



@dp.message_handler(Text(equals="удалить канал"), state='*')
async def cmd_numbers(message: types.Message, state: FSMContext):
    button = []
    global this_id
    this_id = message.from_user.id
    await message.answer("Выберете канал для удаления", reply_markup=get_keyboard())
    global msg
    msg = message
    await state.reset_state()

		
					
@dp.callback_query_handler(Text(startswith="https://t.me/s/"))
async def callbacks_num(call: types.CallbackQuery):
 
    # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
    action = call.data
    file_chat_id = 'users_data.json'
    try:
        with open(file_chat_id) as file_object:
            users_data = json.load(file_object)
    except: users_data = {}
    else:
        del users_data[str(this_id)][action]
        print(users_data)
        with open(file_chat_id, 'w') as file_object:
            json.dump(users_data, file_object)
        await call.message.edit_text(text="Выберете канал для удаления", reply_markup=get_keyboard())
        await call.answer(text="Канал был удалён", show_alert=True)


        
       
      


