class Excecao:
    def __init__(self, frase):
        self.frase = frase

    def imprimir(self):
        return print(self.frase)


class Teste(Excecao):
    def __init__(self, frase):
        super(Teste, self).__init__(frase)
        self.pgt1 = 'a'

    def g(self):
        try:
            self.pgt1 = self.frase
            if '?' not in self.frase:
                raise NotImplementedError('A frase digitada não segue o padrão pedido!')
        except KeyboardInterrupt:
            print('\nO programa foi finalizado em um momento inesperado!')

    def f(self):
        try:
            self.pgt1 = self.frase
            if '?' not in self.frase:
                raise NotImplementedError('A frase digitada não segue o padrão pedido!')
        except KeyboardInterrupt:
            print('\nO programa foi finalizado em um momento inesperado!')
        except TypeError:
            print('Erro encontrado!')

    def imprimir(self):
        return print('-> {}'.format(self.pgt1))


##
pgt = input('Digite uma pergunta: ')
obj = Teste(pgt)
obj.g()

resp = input('Agora, mais uma pergunta: ')
obj2 = Teste(resp)
obj2.g()

print('\nPerguntas:')
obj.imprimir()
obj2.imprimir()
