from Primitives.player import Player
from Primitives.type import Type


class Card(object):
    def __init__(self, name, owner=None):
        """

        :type owner: Player
        """
        super().__init__()
        self.name = name
        self.owner = owner

    @property
    def types(self):
        """

        :rtype: List
        """
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def cost(self):
        raise NotImplementedError

    def play(self):
        raise NotImplementedError


class ManaCard(Card):
    def types(self):
        return [Type.Mana]
