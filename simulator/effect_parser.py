from pyparsing import oneOf, Word, alphas, nums
import yaml

# Game Pieces
COMMODITIES = ['Red', 'Blue', 'Coin']

# ebnf language
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

