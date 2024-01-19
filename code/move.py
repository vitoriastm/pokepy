class Move:
    """
    Properties:
    name = str,
    type = str,
    sound,
    animation,
    damage,
    critical_prob,
    """
    def __init__(self, name, Type, damage, pp, accuracy):
        self.__name = name
        self.__type = Type
        self.__damage = damage
        self.__pp = pp
        self.__accuracy = accuracy

    @property
    def name(self):
        return self.__name

    @property
    def Type(self):
        return self.__type

    @property
    def damage(self):
        return self.__damage

    @property
    def pp(self):
        return self.__pp

    @property
    def accuracy(self):
        return self.__accuracy
