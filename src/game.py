from src.data.board import Board
from src.data.location import Location


class Game:
    def __init__(self):
        self._board: Board

    def move(self, from_pos: Location, to_pos: Location | list[Location] ):
        pass

    def check_victory(self) -> bool:
        pass
