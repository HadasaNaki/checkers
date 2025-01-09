from src.data.location import Location
from src.data.piece import Piece

class Board:
    def __init__(self):
        self._board: list[list[str| Piece]]

    def move(self, from_pos: Location, to_pos: Location | list[Location]):
        pass
