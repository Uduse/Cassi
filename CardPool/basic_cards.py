from Primitives.card import ManaCard
from Primitives.type import Type
from Primitives.player import Player
from Primitives.creature import Creature


class ManaDrop(ManaCard):
    def __init__(self, owner=None):
        super().__init__("Mana Drop", owner)

    def cost(self):
        return 0

    def description(self):
        return "+1 @"

    def play(self):
        self.owner.add_mana(1)


class ManaCrystal(ManaCard):
    def __init__(self, owner=None):
        super().__init__("Mana Crystal", owner)

    def cost(self):
        return 3

    def description(self):
        return "+2 @"

    def play(self):
        self.owner.add_mana(2)


class ManaRock(ManaCard):
    def __init__(self, owner=None):
        super().__init__("Mana Rock", owner)

    def cost(self):
        return 6

    def description(self):
        return "+3 @"

    def play(self):
        self.owner.add_mana(3)


class Slime(Creature):
    def __init__(self, owner=None):
        super().__init__("Slime", 1, 1, owner)

    def cost(self):
        return 2

    def description(self):
        return "Stupid Creature"


class Wolf(Creature):
    def __init__(self, owner=None):
        super().__init__("Wolf", 2, 2, owner)

    def cost(self):
        return 5


class Guard(Creature):
    def __init__(self, owner=None):
        super().__init__("Guard", 3, 3, owner)

    def cost(self):
        return 8


class RanXu(Creature):
    def __init__(self, owner=None):
        super().__init__("Ran Xu", 0, 1, owner)

    def cost(self):
        return 20
