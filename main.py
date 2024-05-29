from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline
from  database.database import initialize_db, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)


initialize_db()



@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я бот о марсе и его спутниках)', reply_markup= get_keyboard_1())
    else:
        await message.answer('Привет, я бот о марсе и его спутниках)', reply_markup=get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'Отправь фото спутника')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://alternathistory.ru/wp-content/uploads/2023/03/Y-MnzOYUDdX1ZC3-01-2048x799.webp', caption= 'Вот ваш спутник!!!', reply_markup=get_keyboard_inline()
                         )

@dp.message_handler(lambda message: message.text == 'перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото планеты', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото планеты')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://narisyu.cdnbro.com/posts/50598450-planeta-mars-kartinki-dlia-detei-29.jpg', caption= 'Вот твоя планета!!!')

@dp.message_handler(lambda message: message.text == 'перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото спутника', reply_markup= get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)
