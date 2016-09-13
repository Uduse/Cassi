from Primitives.card import Card
from Primitives.type import Type


class Creature(Card):
    def __init__(self, name, attack, health, owner=None):
        super().__init__(name, owner)
        self.attack = attack
        self.health = health

    def play(self):
        pass

    def types(self):
        return [Type.Creature]
