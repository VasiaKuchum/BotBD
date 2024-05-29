from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Информация о Фобосе', url='https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D0%B1%D0%BE%D1%81')
    but_inline2 = InlineKeyboardButton('Информация о Деймосе', url='https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%B9%D0%BC%D0%BE%D1%81')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline