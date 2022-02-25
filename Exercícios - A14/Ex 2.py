class Excecao:
    def __init__(self, frase):
        self.frase = frase

    def imprimir(self):
        return print(self.frase)


try:
    msg = input('Digite uma pergunta: ')
    obj = Excecao(msg)
    if '?' not in msg:
        raise NotImplementedError('A frase digitada não segue o padrão pedido!')
except KeyboardInterrupt:
    print('\nO programa foi finalizado em um momento inesperado!')
else:
    obj.imprimir()
