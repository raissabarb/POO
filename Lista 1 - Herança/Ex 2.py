class Mortal:
    def __init__(self):
        self.vivo = ''

    def isVivo(self):
        self.vivo = True
        return self.vivo

    def mata(self):
        self.vivo = False
        return self.vivo


class Gato(Mortal):
    def __init__(self):
        super(Gato, self).__init__()
        self.vivo = super()
        self.cont = 0

    def isVivo(self):
        super().isVivo()
        return self.vivo

    def mata(self):
        self.cont += 1
        if self.cont == 7:
            super().mata()
        return self.vivo

