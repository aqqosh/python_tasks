class Boobs:
    def __init__(self, size):
        self.boobs_size = size

class EnormousBoobs(Boobs):
    def __init__(self):
        super().__init__(size="enourmous")

class BigBoobs(Boobs):
    def __init__(self):
        super().__init__(size="big")
    
class SmallBoobs(Boobs):
    def __init__(self):
        super().__init__(size="small")

class Woman:
    name = ""
    boobs_size = ""
    def __init__(self):
        pass
    def ask_name(self):
        raise AttributeError("Yout haven't asked her name")
    def estimate_boobs(self):
        raise AttributeError("Yout don't know the size of the boobs!")
    def suck_dick(self):
        print("{} sucks your dick".format(self.name))
    def dirty_talk(self):
        print("Oh, I'm a dirty girl")
    def do_titjob(self):
        print("She starts to do a titjob with her {} boobs".format(self.boobs_size))


class HotBrunette(Woman):
    def __init__(self):
        super(Woman, self,).__init__()
    def ask_name(self):
        self.name = "Vitalina"
    def estimate_boobs(self):
        self.boobs_size = BigBoobs()

class AesteticGinger(Woman):
    def __init__(self):
        super(Woman, self).__init__()
    def estimate_boobs(self):
        self.boobs_size = SmallBoobs()


whore = HotBrunette()
whore.estimate_boobs()
whore.ask_name()
whore.dirty_talk()
whore.do_titjob()
whore.suck_dick()