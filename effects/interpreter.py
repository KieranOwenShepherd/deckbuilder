""" For interpreting card effects (in plain english) as directions that need to be taken"""

from lark import Lark, Transformer
from collections import namedtuple

# types of decisions 
# - which card - in hand to discard etc
# - how many of a thing to do
# - do or not (may)
# - choice of a few things (like a switch, probably just don't have this)

#TODO problem: the choice tree requires knowledge of game state
# choosing a card from the hand for example...
# how can the AST present those choices?
# basically, i need to generate a *blank* form 
# For a bot, the simplest thing is to give all possible options for evaluation - a multiple choice form

# TODO possible way to do effects 
# "effect : instruction effect"
# "instruction : gameop STOP" 

# TODO whenever I mention cards, update the context to the last card mentioned

parser = Lark(
    open(r"C:\Users\kiera\Documents\Projects\D-Lite\effects\grammar.lark"),
    start='effect'
)



class EchoEffect(Transformer):
    def __init__(self):
        pass

    def effect(self, items):
        print(items)

    def sentence(self, items):
        return items

    def adj(self, items):
        return "card_type", items[0]

    def verb(self, items):
        print("My verb {}".format(items))



