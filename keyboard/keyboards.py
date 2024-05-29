from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь фото спутника')
    button_2 = KeyboardButton('перейти на следующую клавиатуру')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Отправь фото планеты')
    button_4 = KeyboardButton('перейти на 1 клавиатуру')
    keyboard_2.add(button_3, button_4)
    return keyboard_2