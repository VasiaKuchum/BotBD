from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)






@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый эхо бот', reply_markup= get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/originals/db/46/90/db46900efc60e41a87a1274fecebc977.jpg', caption= 'Вот тебе кот!!!', reply_markup=get_keyboard_inline() )

@dp.message_handler(lambda message: message.text == 'перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.sydneypoint.com.au/wp-content/uploads/2018/07/Top-Dog-Film-Festival-3-1.jpg', caption= 'Вот тебе собака!!!')

@dp.message_handler(lambda message: message.text == 'перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup= get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)
