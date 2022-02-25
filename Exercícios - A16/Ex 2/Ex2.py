class Arquivo:
    def __init__(self):
        pass

    def grava(self, arq_origem, arq_destino):
        ler = arq_origem.read()
        return arq_destino.write(ler)


arq_origem = input('Arquivo com a mensagem a ser anexada: ')
arq_destino = input('Arquivo de destino: ')
arq1 = open("{}".format(arq_origem), "r")
arq2 = open("{}".format(arq_destino), "a+")
gravando = Arquivo()
gravando.grava(arq1, arq2)
print('Objetos na lista 2:')

arq1.close()
arq2.close()
arq2_leitura = open("{}".format(arq_destino), "r")
with arq2_leitura as a:
    for objetos in a:
        print(objetos)
arq2_leitura.close()
