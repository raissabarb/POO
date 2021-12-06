class Mortal:
    def __init__(self):
        self.vivo = ''

    def isVivo(self):
        self.vivo = True
        return self.vivo

    def mata(self):
        self.vivo = False
        return self.vivo


class Ramo(Mortal):
    def __init__(self):
        super(Ramo, self).__init__()

    def ramoDir(self):
        print('O ramo direito foi morto!')

    def ramoEsq(self):
        print('O ramo esquerdo foi morto!')


