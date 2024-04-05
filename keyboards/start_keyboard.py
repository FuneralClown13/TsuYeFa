from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

button_accept = KeyboardButton(text=LEXICON_RU['accept'])
button_reject = KeyboardButton(text=LEXICON_RU['reject'])

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_accept, button_reject]],
                               resize_keyboard=True,
                               one_time_keyboard=True)