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

    def __str__(self):
        return "Gato"


'''
   Caso o System.out.println(g) for chamado, o nome do objeto sera printado na tela, caso o System.out.println(r) para 
um objeto g do tipo Ramo for chamado, nada aparecerá na tela, aliás, aparecerá uma referência ao endereço de memória.
'''