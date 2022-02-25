class Excecao:
    def __init__(self, palavra):
        self.palavra = palavra

    def main(self):
        try:
            str(input('Digite outra palavra: '))
            print('Palavra inicialmente digitada: {}'.format(self.palavra))
        except TypeError:
            print('O que foi digitado não corresponde ao que foi pedido!')
        finally:
            print('Programa finalizado!')


var = input('Digite uma palavra: ')
novo = Excecao(var)
novo.main()
