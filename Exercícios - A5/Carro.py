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
        return print('* Contador incrementado em {} unidades\n'.format(incr))

    def decremento_unidade(self):
        novo_cont = self.cont - 1
        return print('* Contador decrementado em uma unidade\nContador = {}\n'.format(novo_cont))

    def decremento(self, decr):
        novo_cont = self.cont - decr
        return print('* Contador decrementado em {} unidades\nContador = {}\n'.format(decr, novo_cont))

    def contador(self):
        print('\n*** Contador = {}\n'.format(self.cont))


class Carro():

    def __init__(self, m, a, c, aceleracao, frenagem, turnon):
        self.marca = m
        self.ano = a
        self.cor = c
        self.vezesAcelerou = aceleracao
        self.vezesFreou = frenagem
        self.vezesLigou = turnon
        self.atual = 0

    def info_carro(self):
        return print('\nMarca: {}\nCor: {}\nAno: {}'.format(self.marca, self.cor, self.ano))

    def contar(self, num):
        self.vezesAcelerou = num
        return self.vezesAcelerou


numAtual = input('Número atual: ')
numAcel = input('Aceleração: ')
numFren = input('Frenagem: ')
numLigar = input('Quantas vezes ligou: ')
cont1 = Contador(numAtual)
c1 = Carro('Ford', 2019, 'preto', numAcel, numFren, numLigar)
c1.info_carro()
c1.contar(numAcel)
cont1.contador()
print('Quantidade de vezes que acelerou: {}'.format(numAcel))
cont1.incremento(numAcel)
print('Quantidade de vezes que freou: {}'.format(numFren))
cont1.incremento(numFren)
print('Quantidade de vezes que ligou: {}'.format(numLigar))
cont1.incremento(numLigar)
