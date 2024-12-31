from __future__ import annotations

from enum import Enum


class Player(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"
    EMPTY = "EMPTY"

    @classmethod
    def from_str(cls, value: str) -> Player | None:
        if value in ('BLACK', 'WHITE'):
            return cls[value]
        if not value:
            return None
        if isinstance(value, str):
            try:
                return cls[value.replace(" ", "_").upper()]
            except KeyError:
                raise ValueError(f"Invalid Player value: {value}") from None
        raise ValueError(f"Expected str or Player, got {type(value)}")


class State(Enum):
    WHITE_TURN = "WHITE_TURN"
    BLACK_TURN = "BLACK_TURN"
    WHITE_WIN = "WHITE_WIN"
    BLACK_WIN = "BLACK_WIN"

    def is_game_over(self) -> bool:
        return self in (State.WHITE_WIN, State.BLACK_WIN)

    @classmethod
    def from_str(cls, value: str) -> State | None:
        if isinstance(value, State):
            return value
        if not value:
            return None
        if isinstance(value, str):
            try:
                return cls[value.replace(" ", "_").upper()]
            except KeyError:
                raise ValueError(f"Invalid State value: {value}") from None
        raise ValueError(f"Expected str or State, got {type(value)}")
