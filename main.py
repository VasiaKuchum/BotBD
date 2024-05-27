from aiogram import Bot, Dispatcher, types, executor
from config import  TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бот'),
        types.BotCommand(command='/clear', description='Команда для того, чтобы очистить чат'),
        types.BotCommand(command='/friend', description='Команда для того, чтобы подружиться с ботом'),
        types.BotCommand(command='/unfriend', description='Команда для того, чтобы поссорится с ботом'),
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый эхо бот')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу тебе помочь тебе с ....')

@dp.message_handler(commands='clear')
async def clear(message: types.Message):
    await message.answer('Привет, я очищу наш диалог')

@dp.message_handler(commands='friend')
async def friend(message: types.Message):
    await message.answer('Привет, давай подружимся?')

@dp.message_handler(commands='unfriend')
async def unfriend(message: types.Message):
    await message.answer('Привет, давай поссоримся?')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
