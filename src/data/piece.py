from abc import ABC, abstractmethod

from src.data.location import Location

class Piece(ABC):
    @abstractmethod
    def valid_steps(self, pos: Location):
        pass


class Pawn(Piece):
    def valid_steps(self, pos: Location):
        pass


class King(Piece):
    def valid_steps(self, pos: Location):
        pass
