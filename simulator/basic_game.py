from pyparsing import oneOf, Word, alphas, nums
from collections import namedtuple, deque
from itertools import combinations, chain, cycle
import yaml

# Game Pieces
COMMODITIES = ['Red', 'Blue', 'Coin']


# Game structures
Player = namedtuple('Player', ['hand', 'deck', 'tokens'])

Card = namedtuple('Card', ['name', 'cost', 'effect', 'discard_value'])
TokenPool = namedtuple('Token', COMMODITIES)

Game = namedtuple('Game', ['players', 'this_player', 'phase'])

Statement = namedtuple('Statement', ['func', 'words'])


# Effects are made up of statements, and statements modify the game state
# here are some functional building blocks
def move_card(source, dest, n=1):
    dest.extend(source.pop() for _ in range(n))

TOKEN = oneOf(COMMODITIES)
CARD = oneOf('Card Cards')
ELEMENT = TOKEN | CARD
OP = oneOf('+ -')
SHORT_EFFECT = OP + Word(nums) + ELEMENT + '.'

lambda g: move_card(g.this_player.deck, g.this_player.hand, 2)

# Generate cards
def generate_effects():
    """ handy for generating a list of possible effects
    """
    statements = (
        ['+ Card.', '+2 Cards.', '+ Discard.']
        + ['+{n} {token}.'.format(n=n, token=t) for t in COMMODITIES for n in range(1,3)]
    )
    return list(chain(statements, map(' '.join, combinations(statements, 2))))

def yaml_to_cards():


print(generate_effects())

def build_game(num_players=4):
    players = [
            Player(
                deck=deque(),
                tokens=TokenPool(
                    green=0,
                    red=0,
                    black=0,
                    white=0,
                    yellow=0,
                ),
            )
            for n in range(num_players)
    ]

    return Game(
        players=players, 
        this_player=cycle(players),
        phase = cycle([
            'action', 'buy'
        ]),
    )





