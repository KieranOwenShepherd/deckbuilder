
# Ending the game

The game needs to tick down to the end at a fairly constant rate, making play time consistent.

## Tactical play wins.

Wingspan is mysterious, which birds are actually good? 
Chess isn't mysterious on face, it's obvious which piece is the best,
the key is making the best use of all of them.

## Require less copies of each card.

Why - less pricy, smaller, and more diverse game.

- Problems with one copy of each card (Wingspan, Ascension).
Multiple copies of each card creates an auto balancing system.
Knowledge is then the thing that separates players most.

Card balance is a difficult aspect of design, without imbalance everything is vanilla.
At its worst a single copy of a very good card means that a player that gets to the card through luck
automatically wins the game.

Counters can provide some balance (moat), but must always be available.
Inherent weakness, like `Raven` or `Deal Breaker`
Shifting priorities through the game also provide some balance.

## Easier to read the cards

Andrews pulling one copy of each aside I still find frustrating.
I have to make all the cards within easy reading.

## Interactivity

Dominion is a game multiple people play alone. It's too solitary.
That could have been avoided with careful cultivation of effects,
however, the greatest change was made with artifacts.
Interactivity is cleaner if built into the fundamentals of the game.

## Make a game Loren enjoys

Loren uses games to relax, she doesn't want to discuss strategy, she wants to be able to mindlessly
play and sometimes win. 
I am full of curiosity, I want to try different things, explore, and see how it turns out. I don't mind if I lose sometimes. I do like to win though, and optimize.
Andrew loves to win strategies and optimize.

## Bring back surprise

Hidden information following clues, the aha moment, these are all what makes Biblios so engaging.

# Actions with attachments

This mechanic started as a way to formalize a trade without the bartering process.
The turn player has an option to use some effect, while doing so give the opponent the opportunity to do so as well.

Instead, I'll make core mechanics of the game accessible through these actions.
Buy a card.

I might need to find a better word than action.

## balancing

On a persons turn they can choose an action to do.
At this time, any attached actions activate, and their owners follow their instructions in order starting with the player next to the turn player.
The cards then become played. (or perhaps we could trash them)

# Paying

Pay (value) is useful, it gives the option to discard a card or use your expendable commodities

# Colored Currencies

Each commodity acts uniquely

## Red 
gaining red currency in this adds cards to your hand from the red pile (maybe 20 total).
most of these cards have very superfluous effects, limiting their use, but paying with them sends them back to the pile.
- you don't want them in your discard pile
    - this means players need to act carefully to spend them all
    - it can also be a punishment to force players to take them

## Gold
accumulates as tokens when gaining
perhaps as too many are gained there could be backlash (reduce by half ala Catan)

## Blue
Cards can't be discarded for blue, you can only get it by playing effects.

# More Artifacts

A power that players temporarily hold, that's really useful interactivity.

One careful thing about the design from dominion is that they always continue to progress the game.


# Programming card movement

Playing a card 
- remove from one tuple add to another
Drawing a card 
Shuffling cards

There's two types of places cards go; 
- decks - ordered, hidden - deck, other deck
- areas - unordered, visible - hand, trash, in_play, attached, sidedeck

a tuple works fine for decks
frozenset almost works fine for areas except that it doesn't support duplicates

I could turn off equality testing for cards

# Strategy of keeping cards

I want trashing of starter cards to be a more difficult decision.
If you can always get them back whenever you want, it's not a tough decision.

# Swapping out cards

I want to keep the game light

# Categories

They always seem to help.
We can create categories with effect text, costs and discard values.
However, the symbology for that is tougher.