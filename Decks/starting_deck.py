from Primitives.basic_piles import Deck
from CardPool.basic_cards import *


class StartingDeck(Deck):
    def __init__(self, owner=None):
        super().__init__(owner)
        self.cards.extend([ManaCrystal() for _ in range(8)])
        self.cards.extend([Slime() for _ in range(4)])
