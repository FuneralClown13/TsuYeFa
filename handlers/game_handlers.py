from aiogram import Router
from aiogram.types import Message
from filters.game_filter import GameFilter
from services.game_logic import Game
from lexicon.lexicon import LEXICON_RU, SKINS
from keyboards import game_keyboard, start_keyboard

router = Router()


@router.message(GameFilter())
async def send_echo(message: Message):
    game = Game(message.text)
    game.run()

    await message.answer(text=SKINS['bot_skins'][game.bot_motion])
    await message.answer(text=f'{LEXICON_RU[game.result]}\n'
                              f'{LEXICON_RU['reply']}',
                         reply_markup=game_keyboard.keyboard)
