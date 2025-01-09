from abc import ABC, abstractmethod

from src.data.location import Location
from src.data.enumes import Colors

class Piece(ABC):
    def __init__(self, color: Colors, location: Location):
        self.color_player: Colors = color
        self.location_layer: Location = location

    @abstractmethod
    def valid_steps(self) -> list[Location | list[Location]]:
        pass


class Pawn(Piece):
    def valid_steps(self) -> list[Location | list[Location]]:
        pass


class King(Pawn):
    def valid_steps(self) -> list[Location | list[Location]]:
        pass
