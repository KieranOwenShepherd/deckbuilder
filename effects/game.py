"""
Dlite is the codename for a deck building game, building upon concepts established by 
predecessors like Dominion.
The main goals of dlite are to
    - Increase player interraction
    - Add a deeper tactical layer to deckbuilding
    - Reduce passive waiting time for players
"""

import cards
import pandas as pd


class Game:
    """Describes the entire state of the game"""

    def __init__(self, number_of_players):
        self.players = pd.Dataframe()
        self.cards = pd.Dataframe()

