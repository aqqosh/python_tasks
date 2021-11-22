class Alphabet:
    def __repr_(self):
        return self.__str__()

class EnglishAlphabet(Alphabet):
    def __str__(self) -> str:
        return "English alphabet"

class GeorgianAlphabet(Alphabet):
    def __str__(self) -> str:
        return "Georgian alphabet"

class RussianAlphabet(Alphabet):
    def __str__(self) -> str:
        return "Russian alphabet"

class Language:
    alphabet = ""
    def __str__(self):
        return self.alphabet.__str__()
    def __repr__(self):
        return self.alphabet.__repr__()
    def set_alphabet(self):
        raise AttributeError("No Implemented Alphabet")

class EnglishLanguage(Language):
    def set_alphabet(self):
        self.alphabet = EnglishAlphabet()

class GeorgianAlphabet(Language):
    def set_alphabet(self):
        self.alphabet = GeorgianAlphabet()

class RussianAlphabet(Language):
    def set_alphabet(self):
        self.alphabet = RussianAlphabet()

l1 = EnglishLanguage()
l1.set_alphabet()
print(str(l1))