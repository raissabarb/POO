class Contador:

    def __init__(self, val_atual):
        self.cont = val_atual

    def get_contador(self):
        conta = self.cont
        return print('O contador está em: {}'.format(conta))

    def incremento_unidade(self):
        novo_cont = self.cont + 1
        return print('* Contador incrementado em uma unidade\nContador = {}\n'.format(novo_cont))

    def incremento(self, incr):
        novo_cont = self.cont + incr
        return print('* Contador incrementado em {} unidades\nContador = {}\n'.format(incr, novo_cont))

    def decremento_unidade(self):
        novo_cont = self.cont - 1
        return print('* Contador decrementado em uma unidade\nContador = {}\n'.format(novo_cont))

    def decremento(self, decr):
        novo_cont = self.cont - decr
        return print('* Contador decrementado em {} unidades\nContador = {}\n'.format(decr, novo_cont))

    def contador(self):
        print('*** Contador = {}\n'.format(self.cont))


cont1 = Contador(0)
cont1.contador()
cont1.incremento_unidade()
cont1.decremento_unidade()
cont1.incremento(2)
cont1.decremento(1)

print('----------------------------------------')

cont2 = Contador(8)
cont2.contador()
cont2.incremento_unidade()
cont2.decremento_unidade()
cont2.incremento(4)
cont2.decremento(2)
