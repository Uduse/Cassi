import DataBase.basic_decks as starting_deck
import Primitives.pile as pile


class Player(object):
    def __init__(self, name, game, deck=None, hand=None, discard=None, in_play=None):
        """

        :type name: object
        """
        super().__init__()
        self.name = name
        self.game = game

        if not hand:
            self.hand = pile.EmptyDiscard()
        if not discard:
            self.discard = pile.EmptyDiscard()
        if not deck:
            self.deck = starting_deck.StartingDeck
        if not in_play:
            self.in_play = pile.InPlay()

        self.action = 0
        self.mana = 0
        self.cast = 0

    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            self.draw_one_card()

    def draw_one_card(self):
        if self.deck.has_card():
            self.hand.add_card(self.deck.get_a_card_from_top())
        elif self.discard.has_card():
            self.reshuffle_discard_to_deck()
            self.hand.add_card(self.deck.get_a_card_from_top())

    def reshuffle_discard_to_deck(self):
        self.discard.shuffle()
        self.deck.add_cards(self.discard.cards)
        self.discard.clear()

    def init_turn(self):
        self.action = 1
        self.cast = 1
        self.mana = 0

    def add_mana(self, num=1):
        self.mana += num

    def take_turn(self):
        self.init_turn()
        self.action_phase()
        self.cast_phase()
        self.clean_up_phase()

    def action_phase(self):
        pass

    def cast_phase(self):
        while True:
            user_input = input("Press SPACE to use all mana.\n"
                               "Press number keys to select spells.\n")
            if user_input == " ":
                self.play_all_mana_cards()

    def clean_up_phase(self):
        self.discard_hand()

    def play_all_mana_cards(self):
        pass

    def discard_hand(self):
        self.discard.add_cards(self.hand.cards)
        self.hand.cards.clear()

    def redraw_hand(self, num_cards=6):
        self.draw_cards(num_cards)
