from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import SKINS

button_rock = KeyboardButton(text=SKINS['user_skins']['rock'])
button_paper = KeyboardButton(text=SKINS['user_skins']['paper'])
button_scissors = KeyboardButton(text=SKINS['user_skins']['scissors'])

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_rock, button_paper, button_scissors]], resize_keyboard=True)