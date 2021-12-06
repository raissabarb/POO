class Mortal:
    def __init__(self):
        self.vivo = ''

    def isVivo(self):
        self.vivo = True
        return self.vivo

    def mata(self):
        self.vivo = False
        return self.vivo
