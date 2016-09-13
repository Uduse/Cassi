import random


class Pile(object):
    def __init__(self, owner=None):
        super().__init__()
        self.cards = []
        self.owner = owner

    def has_card(self):
        return len(self.cards) != 0

    @property
    def num_cards(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def clear(self):
        self.cards.clear()

    def shuffle(self):
        random.shuffle(self.cards)
