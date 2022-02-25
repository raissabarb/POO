class interfaceGravaPalavra:  # classe com o mesmo intuito da interface em Java
    def __init__(self):
        pass

    def adiciona_palavra(self, palavra, contador):
        pass


class gravaPalavra:
    def __init__(self):
        pass

    def adiciona_palavra(self, palavra, contador, lista1, lista2):
        lista1.append(palavra)
        lista2.append(contador)


listaPalavras = []
listaContador = []

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

for i in range(0, 3):
    print(listaPalavras[i] + ' - ' + listaContador[i])
