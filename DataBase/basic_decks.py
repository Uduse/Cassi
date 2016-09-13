import Primitives.pile as pile
import DataBase.basic_cards as cards


class StartingDeck(pile.Deck):
    def __init__(self, owner=None):
        super().__init__(owner)
        self.cards.extend([cards.ManaCrystal() for _ in range(8)])
        self.cards.extend([cards.Slime() for _ in range(4)])
