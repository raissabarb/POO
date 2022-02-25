arquivo = open("lista_ex3.txt", "r")
cont = 0
with arquivo as arq:
    for linha in arq:
        cont += 1
        print('Palavra {} - {}'.format(cont, linha))
arquivo.close()
