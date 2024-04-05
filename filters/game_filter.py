from aiogram.filters import Filter
from aiogram.types import Message
from lexicon.lexicon import SKINS

class GameFilter(Filter):
    async def __call__(self, message: Message):
        return message.text in SKINS['user_skins'].values()
