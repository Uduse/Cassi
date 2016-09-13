import Primitives.player as player
import DataBase.basic_decks as decks


class Game(object):
    def __init__(self, num_players):
        super().__init__()
        self.players = []
        for index in range(num_players):
            self.players.append(player.Player(str(index), self))
        self.num_players = num_players
        self.turn_counter = 0
        self.set_up()
        self.game_start()

    def set_up(self):
        for p in self.players:
            p.deck = decks.StartingDeck()
            p.deck.shuffle()

    def game_start(self):
        while not self.game_ends():
            for p in self.players:
                p.take_turn()
                self.turn_counter += 1

    def game_ends(self):
        return self.turn_counter >= 20

        # def log(func):
        #     def wrapper(*args, **kwargs):
        #         func(*args, **kwargs)
        #         return
        #     return wrapper
