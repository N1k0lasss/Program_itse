#   LSP
#   Liskov Substitution Principle (Principio de Sustitución de Liskov)
#   Una clase debe ser substitutable por una subclase
#   y una subclase debe ser substitutable por una clase

class ave():
    pass


class ave_voladora(ave):
    def volar(self):
        print("Voy volando")


class ave_no_voladora(ave):
    pass
