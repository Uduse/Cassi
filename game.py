from Primitives.player import Player
from Decks.starting_deck import StartingDeck


class Game(object):
    def __init__(self, num_players):
        super().__init__()
        self.players = [Player() for _ in range(self.num_players)]
        self.num_players = num_players
        self.set_up()
        self.game_start()
        self.turn_counter = 0

    def set_up(self):
        for player in self.players:
            player.deck = StartingDeck()
            player.deck.shuffle()

    def game_start(self):
        while not self.game_ends():
            for player in self.players:
                player.take_turn()
                self.turn_counter += 1

    def game_ends(self):
        return self.turn_counter >= 20

        # def log(func):
        #     def wrapper(*args, **kwargs):
        #         func(*args, **kwargs)
        #         return
        #     return wrapper
