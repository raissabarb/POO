class No:
    def __init__(self, item=None):
        self.item = item
        self.proximo = None


class Lista:
    def __init__(self):
        self.primeiro = No()
        self.ultimo = self.primeiro
        self.tam = 0

    def inserir(self, item):
        self.ultimo.proximo = No(item)
        self.ultimo = self.ultimo.proximo
        self.tam += 1

    def buscar(self, item):
        if self.tam == 0:
            mensagem = "Lista vazia."
            return mensagem
        busca = self.primeiro.proximo
        while busca is not None and busca.item != item:
            busca = busca.proximo
        try:
            if busca.item == item:
                return True
        except:
            return False

    def remover(self):
        if self.tam == 0:
            mensagem = "Lista vazia."
            return mensagem
        remove2 = self.primeiro
        while remove2.proximo != self.ultimo:
            remove2 = remove2.proximo
        item = self.ultimo.item
        ultimo = remove2
        remove2 = ultimo.proximo
        ultimo.proximo = None
        del remove2
        self.tam -= 1
        return item

    def soma_inteiros(self):
        aux = self.primeiro.proximo
        soma = 0
        cont = 0
        while cont < self.tam:
            soma += aux.item
            aux = aux.proximo
            cont += 1
        return soma


teste = Lista()
teste.inserir(5)
teste.inserir(19)
teste.inserir(26)
print(teste.soma_inteiros())