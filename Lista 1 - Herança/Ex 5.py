class Mortal:
    def __init__(self):
        self.vivo = ''
        self.aux2 = 0

    def isVivo(self):
        self.vivo = True
        return self.vivo

    def mata(self):
        self.vivo = False
        self.aux2 += 1
        return self.vivo


class Ramo(Mortal):
    def __init__(self):
        super(Ramo, self).__init__()

    def ramoDir(self):
        return print('O ramo direito foi morto!')

    def ramoEsq(self):
        return print('O ramo esquerdo foi morto!')


class Gato(Mortal):
    def __init__(self):
        super(Gato, self).__init__()
        self.vivo = super()
        self.cont = 0
        self.aux = 0

    def isVivo(self):
        super().isVivo()
        return self.vivo

    def mata(self):
        self.cont += 1
        if self.cont == 7:
            super().mata()
        self.aux += 1
        return self.vivo

    def __str__(self):
        return "Gato"


cabra = Mortal()
info1 = cabra.isVivo()
info2 = cabra.mata()
print(info1)
print(info2)

print('\n')
gato = Gato()
info1 = gato.isVivo()
info2 = gato.mata()
print(info1)
print(info2)
info21 = gato.mata()
info22 = gato.mata()
info23 = gato.mata()
info24 = gato.mata()
info25 = gato.mata()
info26 = gato.mata()
print(info25)  # sexta tentativa chamando o método mata()
print(info26)  # sétima tentativa do método, tornando o status do gato como False

print('\n')
print(cabra)  # Teste para a pergunta do enunciado
print(gato)

r = Ramo()
r.mata()
r.mata()
if r.aux2 <= 2:
    r.ramoDir()
elif r.aux2 > 2:
    r.ramoEsq()

print('\n')
r2 = Ramo()
r2.mata()
r2.mata()
r2.mata()
if r2.aux2 <= 2:
    r2.ramoDir()
elif r2.aux2 > 2:
    r2.ramoEsq()