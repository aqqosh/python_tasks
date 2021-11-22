"""
Классу заранее неизвестно, объекты каких подклассов ему нужно создать.
Обязанности делегируются подклассу, а знания о том, какой подкласс принимает эти обязанности, локализованы.
Создаваемые объекты родительского класса специализируются подклассами.
"""

"""
Продукт 
Определяет общий интерфейс объектов, которые может 
произвести создатель и его подклассы.
"""
class Culture:
    """Description"""
    def __repr__(self):
        return self.__str__()

"""
Конкретные продукты 
Cодержат код различных продуктов. Продукты будут отличаться 
реализацией, но интерфейс у них будет общий.
"""

class Democracy(Culture):
    def __str__(self):
        return "Democracy"

class Dictatiorship(Culture):
    def __str__(self):
        return "Dictatorship"

"""
Создатель
Объявляет фабричный метод, который должен возвращать новые объекты продуктов. 
Важно, чтобы тип результата совпадал с общим интерфейсом продуктов.
Зачастую фабричный метод объявляют абстрактным, чтобы заставить все подклассы реализовать 
его по-своему. Но он может возвращать и некий стандартный продукт.
"""

class Government:
    """Description"""
    culture = ""
    def __str__(self):
        return self.culture.__str__()

    def __repr__(self):
        return self.culture.__repr__()

    def set_culture(self):
        raise AttributeError("No Implemented Culture")

"""
Конкретные создатели
По-своему реализуют фабричный метод, производя те или иные конкретные продукты.
Фабричный метод не обязан всё время создавать новые объекты. Его можно переписать 
так, чтобы возвращать существующие объекты из какого-то хранилища или кэша.
"""

class GovernmentA(Government):
    def set_culture(self):
        self.culture = Democracy()

class GovernmentB(Government):
    def set_culture(self):
        self.culture = Dictatiorship()

"""
Пример
"""

g1 = GovernmentA()
g1.set_culture()
print(str(g1))

g2 = GovernmentB()
g2.set_culture()
print(str(g2))