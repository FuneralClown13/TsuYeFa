from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards import game_keyboard, start_keyboard

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=start_keyboard.keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])



# Этот хэндлер срабатывает на согласие поиграть
@router.message(F.text == (LEXICON_RU['accept']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['accept_message'],
                         reply_markup=game_keyboard.keyboard)


# Этот хэндлер срабатывает на отказ поиграть
@router.message(F.text == LEXICON_RU['reject'])
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['reject_message'])

