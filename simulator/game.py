from itertools import combinations, chain, cycle
from collections_extended import frozenbag
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable

# Fundamentals

class Currency(Enum):
    NONE = 0
    RED = 1
    YELLOW = 2
    BLUE = 3    

@dataclass(eq=True, frozen=True)
class Effect():
    instruction : str

# Cards

@dataclass(eq=True, frozen=True)
class Action():
    name : str
    effect : Effect

@dataclass(eq=True, frozen=True)
class Card():
    name : str
    currency : Currency
    cost : str
    effect : Effect

# Game

@dataclass(frozen=True)
class Area():
    cards : tuple[Card, ...]

    def __eq__(self, other):
        return sorted(self.cards) == sorted(other)

area = frozenbag[Card]

@dataclass(eq=True, frozen=True)
class Player():
    deck : tuple[Card, ...]
    discard : area
    sidedeck : area
    in_play : area
    hand : area

@dataclass(eq=True, frozen=True)
class Game():
    "class for keeping game state"
    players : tuple[Player, ...]
    actions : tuple[Action, ...]
    trash : area
    turn_player : Iterable[tuple[Player, ...]] = field(init=False)

    def __post_init__(self):
        self.turn_player = cycle(self.players)


# use replace like dict.update