class Estoque:
    def __init__(self):
        pass

    def novo_arq(self, arq1, arq2, arq3):
        prim = arq1.read()
        seg = arq2.read()
        arq3.write(prim)
        arq3.write(seg)

    def ordena(self, arq):
        ler_arq = open("{}".format(arq), "r")
        lista_aux = []
        with ler_arq as ler:
            for line in ler:
                lista_aux.append(line)
        ler_arq.close()
        lista_aux.sort()
        arq_ordenado = open("{}".format(arq), "w")
        tam = len(lista_aux)
        for i in range(tam):
            arq_ordenado.write(lista_aux[i])
        arq_ordenado.close()


narq = "itens3.dat"
arq_novo = open(narq, "a+")
arq_or1 = "itens1.dat"
arq_or2 = "itens2.dat"
arq1 = open(arq_or1, "r")
arq2 = open(arq_or2, "r")
novo = Estoque()
novo.novo_arq(arq1, arq2, arq_novo)  # Precisando rodar duas vezes para ter o resultado desejado
novo.ordena(narq)
arq_novo.close()
arq1.close()
arq2.close()
