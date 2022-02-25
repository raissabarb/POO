class interfaceGravaPalavra:  # classe com o mesmo intuito da interface em Java
    def __init__(self):
        pass

    def adiciona_palavra(self, palavra, contador):
        pass

    def gravar_palavra(self, palavra, contador, arquivo):
        pass


class gravaPalavra:
    def __init__(self):
        pass

    def adiciona_palavra(self, palavra, contador, lista1, lista2):
        lista1.append(palavra)
        lista2.append(contador)

    def gravar_palavra(self, palavra, contador, arquivo):
        arquivo.write(palavra + ' -> ' + contador + '\n')


listaPalavras = []
listaContador = []
nomeArq = input('Nome do arquivo: ')
nome = nomeArq + '.txt'
arq = open("{}".format(nome), "a+")

# Item um
p1 = input('Palavra: ')
cont1 = input('Contador: ')
np = gravaPalavra()
np.adiciona_palavra(p1, cont1, listaPalavras, listaContador)

# Item dois
p2 = input('Palavra: ')
cont2 = input('Contador: ')
np2 = gravaPalavra()
np2.adiciona_palavra(p2, cont2, listaPalavras, listaContador)

# Item três
p3 = input('Palavra: ')
cont3 = input('Contador: ')
np3 = gravaPalavra()
np3.adiciona_palavra(p3, cont3, listaPalavras, listaContador)

# Colocando as palavras num arquivo
gravando = gravaPalavra()
for i in range(0, 3):
    gravando.gravar_palavra(listaPalavras[i], listaContador[i], arq)
arq.close()

# Lendo arquivo criado
arq_leitura = open("{}".format(nome), "r")
print('\n')
with arq_leitura as arquivo:
    for palavra in arq_leitura:
        print(palavra)
arq_leitura.close()
