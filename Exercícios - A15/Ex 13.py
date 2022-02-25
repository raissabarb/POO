class ContadorDePalavras:
    def __init__(self):
        pass

    def adiciona(self, palavra, lista):
        lista.append(palavra)
        return lista

    def contar(self, palavra, lista):
        tam = len(lista)
        cont = 0
        for i in range(0, tam):
            aux = lista[i]
            if aux == palavra:
                cont += 1
        return cont


lista = []
teste = ContadorDePalavras()
teste.adiciona('macaco', lista)
teste.adiciona('baleia', lista)
teste.adiciona('leão', lista)
teste.adiciona('macaco', lista)
teste.adiciona('borboleta', lista)
palavra = input('Qual palavra deseja contabilizar? ')
num = teste.contar(palavra, lista)
print('A palavra "{}" apareceu {} vezes na lista'.format(palavra, num))
