from random import choice
from lexicon.lexicon import SKINS


class Game:
    MOTIONS = ['rock', 'paper', 'scissors']
    GAME_RULES = {
        'rock': {'rock': 'draw', 'scissors': 'win', 'paper': 'lose'},
        'scissors': {'rock': 'lose', 'scissors': 'draw', 'paper': 'win'},
        'paper': {'rock': 'win', 'scissors': 'lose', 'paper': 'draw'}
    }

    def __init__(self, player_motion):
        self.player_motion = self.__representation_player_motion(player_motion)
        self.bot_motion: str
        self.result: str

    def run(self):
        self.bot_motion = self.__get_random_motion()
        self.result = self.__get_result_game(self.player_motion, self.bot_motion)

    def __get_random_motion(self) -> str:
        return choice(self.MOTIONS)

    def __get_result_game(self, player_motion, bot_motion) -> str:
        return self.GAME_RULES[player_motion][bot_motion]

    def __representation_player_motion(self, player_motion):
        for key in SKINS['user_skins'].keys():
            if SKINS['user_skins'][key] == player_motion:
                return key
