from src.data.enumes import State
from src.game import Game


class Play:
    def __init__(self):
        self.game: Game
        self.game_status: State

    def play(self):
        pass

    def get_moves(self) -> str | list[str]:
        pass
