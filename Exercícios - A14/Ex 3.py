class Excecao:
    def __init__(self, frase):
        self.frase = frase

    def imprimir(self):
        return print(self.frase)


class Teste(Excecao):
    def __init__(self, frase):
        super(Teste, self).__init__(frase)

    def imprimir(self):
        super().imprimir()


try:
    pgt = input('Digite uma pergunta: ')
    obj = Teste(pgt)
    if '?' not in pgt:
        raise NotImplementedError('A frase digitada não segue o padrão pedido!')
    resp = input('Agora, digite a resposta da sua pergunta: ')
    obj2 = Teste(resp)
    if '.' not in resp:
        raise NotImplementedError('A frase digitada não segue o padrão pedido!')
except KeyboardInterrupt:
    print('\nO programa foi finalizado em um momento inesperado!')
else:
    obj.imprimir()
    obj2.imprimir()
    print('Finalizando...')

