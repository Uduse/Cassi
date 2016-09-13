import names


class Figure(object):
    def __init__(self, name=None):
        super().__init__()
        self._name = name if name else Figure.random_name()

    @classmethod
    def random_name(cls):
        return names.get_full_name()
