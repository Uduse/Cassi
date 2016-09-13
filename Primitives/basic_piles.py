from Primitives.card import Card
from Primitives.pile import Pile


class Deck(Pile):
    def __init__(self, owner=None):
        super().__init__(owner)

    def add_to_top(self, card):
        self.cards.append(card)

    def get_a_card_from_top(self):
        """

        :rtype: Card
        """
        if not self.cards:
            raise ValueError("No Card on top")
        else:
            return self.cards.pop()


class Hand(Pile):
    pass


class EmptyHand(Hand):
    pass


class Discard(Pile):
    pass


class EmptyDiscard(Discard):
    pass


class InPlay(Pile):
    pass

# def draw_cards_from_top(self, num_cards):
#     for _ in range(num_cards):
#         self.draw_a_card_from_top()
