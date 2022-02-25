class Arquivo:
    def __init__(self):
        pass

    def verificar(self, prim, seg):
        arq1_aberto = open("{}".format(prim), "r")
        arq2_aberto = open("{}".format(seg), "r")
        lista1 = []
        compara1 = []
        lista2 = []
        compara2 = []
        aux = []
        aux2 = []
        cont = 0
        with arq1_aberto as file:
            for line in file:
                for word in line.split():
                    palavra_arq1 = word
                    aux.append(palavra_arq1)
        with arq2_aberto as file2:
            for line2 in file2:
                for word2 in line2.split():
                    palavra_arq2 = word2
                    aux2.append(palavra_arq2)
        for i in range(0, len(aux)-4):
            lista1.append(aux[i])
            lista1.append(aux[i+1])
            lista1.append(aux[i+2])
            lista1.append(aux[i+3])
            lista1.append(aux[i+4])
            compara1.append(lista1)
            for j in range(0, len(aux2)-4):
                lista2.append(aux2[j])
                lista2.append(aux2[j+1])
                lista2.append(aux2[j+2])
                lista2.append(aux2[j+3])
                lista2.append(aux2[j+4])
                compara2.append(lista2)
                if compara2 == compara1:
                    cont = 1
                else:
                    lista2.clear()
                    compara2.clear()
            lista1.clear()
            compara1.clear()
        arq1_aberto.close()
        arq2_aberto.close()
        return cont


arq1 = input('Nome do primeiro arquivo: ')
arq2 = input('Nome do segundo arquivo: ')
consulta = Arquivo()
resposta = consulta.verificar(arq1, arq2)
if resposta == 1:
    print('HÁ pelo menos uma sequência com 5 ou mais palavras presentes em ambos os arquivos!')
else:
    print('NÃO há semelhança entre as sequências!')
