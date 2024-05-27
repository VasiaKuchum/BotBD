from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://aliexpress.ru/?acnt=103863733&src=yandex&aff_short_key=_9zpFKc&aff_platform=true&cn=109269429&utm_source=yandex&utm_medium=cpc&utm_campaign=JVRU_ALI_YANDEX_WEB_UA_RU(ALL)_SEARCH_BRAND&utm_content=_&yclid=10548804494927593471')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://aliexpress.ru/?acnt=103863733&src=yandex&aff_short_key=_9zpFKc&aff_platform=true&cn=109269429&utm_source=yandex&utm_medium=cpc&utm_campaign=JVRU_ALI_YANDEX_WEB_UA_RU(ALL)_SEARCH_BRAND&utm_content=_&yclid=10548804494927593471')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline