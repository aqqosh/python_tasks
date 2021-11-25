class Woman():
    """
    Interface
    """
    def do_blowjob(self) -> str:
        pass
    def do_titjob(self) -> str:
        pass

class Brunette(Woman):
    """
    Concrete Component
    """
    def do_blowjob(self) -> str:
        return "And that Brunette does you a blowjob"
    def do_titjob(self) -> str:
        return "And that Brunette does you a titjob"

class Decorator(Woman):
    _woman: Woman = None

    def __init__(self, woman: Woman) -> None:
        self._woman = woman

    @property
    def woman(self) -> str:
        return self._woman

    def do_blowjob(self) -> str:
        return self._woman.do_blowjob()

    def do_titjob(self) -> str:
        return self._woman.do_titjob()

class Japanese(Decorator):
    def do_blowjob(self) -> str:
        return "She has hot japanese mouth. " + self.woman.do_blowjob()
    def do_titjob(self) -> str:
        return "She has big japanese boobs. " + self.woman.do_titjob()

class Young(Decorator):
    def do_blowjob(self) -> str:
        return "The woman you see is very young. " + self.woman.do_blowjob()
    def do_titjob(self) -> str:
        return "The woman you see is very young. " + self.woman.do_titjob()

if __name__ == "__main__":
    random_brunette = Brunette()
    random_brunette.do_blowjob()

    japanese_brunette = Japanese(random_brunette)
    young_japanese_brunette = Young(japanese_brunette)
    young_japanese_brunette.do_blowjob()
