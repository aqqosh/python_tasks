""" Types """

class Culture:
    """Description"""
    def __repr__(self):
        return self.__str__()

class Democracy(Culture):
    def __str__(self):
        return "Democracy"

class Dictatiorship(Culture):
    def __str__(self):
        return "Dictatorship"

class Government:
    """Description"""
    culture = ""
    def __str__(self):
        return self.culture.__str__()

    def __repr__(self):
        return self.culture.__repr__()

    def set_culture(self):
        raise AttributeError("No Implemented Culture")

class GovernmentA(Government):
    def set_culture(self):
        self.culture = Democracy()

class GovernmentB(Government):
    def set_culture(self):
        self.culture = Dictatiorship()

g1 = GovernmentA()
g1.set_culture()
print(str(g1))

g2 = GovernmentB()
g1.set_culture()
print(str(g2))