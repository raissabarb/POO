class Conta:

    saldo = float
    numero = int

    def __init__(self, a):
        self.saldo = 0
        self.numero = a
        self.qtd = 0

    def debita(self, quantia):
        self.qtd = quantia
        if self.qtd > 0:
            self.saldo += self.qtd
        else:
            print('Conta.depositar(...): ' + 'não se pode depositar uma quantia negativa')

    def credita(self, quantia):
        if quantia > 0:
            self.saldo -= quantia
        else:
            print('Conta.saca(...)' + 'não se pode sacar uma quantia negativa')

    def get_saldo(self):
        return self.saldo

    def get_numero(self):
        return self.numero

    def imprime(self):
        return print('- Conta {}: saldo = {}'.format(self.numero, self.saldo))


class ContaPoupanca(Conta):
    def __init__(self, a, juros):
        super(ContaPoupanca, self).__init__(a)
        self.juros = juros/100
        self.cont = 1

    def get_saldo(self):
        novo_saldo = super().get_saldo()
        novo_saldo += novo_saldo * self.juros
        return novo_saldo

    def imprime(self):
        super().imprime()


class ContaCorrente(Conta):
    def __init__(self, a, lim):
        super(ContaCorrente, self).__init__(a)
        self.lim = lim

    def credita(self, quantia):
        saldo_atual = super().get_saldo()
        val_limite = self.lim + saldo_atual
        if val_limite - quantia >= 0:
            super().credita(quantia)
            print('* O valor de R${} foi creditado com sucesso!\n'.format(quantia))
        else:
            valor_estourado = quantia - val_limite
            print('*** Cuidado ***\nNão foi possível fazer a operação!\nLimite de R${} estourado em R${}!\n'.format(self.lim, valor_estourado))

    def imprime(self):
        super().imprime()


class Banco():

    contas = list()

    def __init__(self):
        self.nova_conta = 0
        self.conta_analisada = 0
        self.novo_lim = 0
        self.novo_juros = 0

    def adicionar(self, usuario):
        self.contas.append(usuario)

    def mostrar_contas(self):
        for conta in self.contas:
            return conta

    def atualiza(self):
        print('Ação realizada!')

    def abrir_conta_corrente(self, a, limite):
        self.nova_conta = a
        self.novo_lim = limite
        return self.nova_conta and self.novo_lim

    def abrir_conta_poupanca(self, a, juros):
        self.nova_conta = a
        self.novo_juros = juros
        return self.nova_conta and self.novo_juros

    def apagar(self, usuario):
        cont = 1
        for conta in self.contas:
            if conta == usuario:
                self.contas.pop(cont)
            cont += cont

    def fechar_conta(self, a):
        self.conta_analisada = a
        return self.conta_analisada

    def dividendo(self, juros):
        self.novo_juros = juros
        return self.novo_juros


usuario1 = Conta(245)
usuario1.debita(25.50)
usuario1.debita(50)
saldo = usuario1.get_saldo()

usuario2 = ContaCorrente(300, 300)
usuario2.credita(200)
usuario2.credita(500)
usuario2.credita(50)

usuario3 = ContaPoupanca(301, 5)
usuario3.credita(100)
usuario3.debita(105)

banco1 = Banco()
banco1.adicionar(usuario1.imprime())
banco1.adicionar(usuario2.imprime())
banco1.adicionar(usuario3.imprime())
banco1.mostrar_contas()
banco1.atualiza()
opc = int(input('\nCorrente (1) ou poupança (2)? '))
if opc == 1:
    banco1.abrir_conta_corrente(302, 200)
    usuario4 = ContaCorrente(302, 200)
    usuario4.debita(100)
    usuario4.credita(10)
    banco1.adicionar(usuario4.imprime())
    banco1.mostrar_contas()
elif opc == 2:
    banco1.abrir_conta_poupanca(302, 7.5)
    usuario4 = ContaCorrente(302, 7.5)
    usuario4.debita(200)
    usuario4.credita(25.90)
    banco1.adicionar(usuario4.imprime())
    banco1.mostrar_contas()
escolha = banco1.dividendo(2)
usuario5 = ContaPoupanca(303, escolha)
usuario5.debita(55)
print('\nSaldo após pagamento de dividendo da Conta Poupança: {}'.format(usuario5.get_saldo()))
escolha2 = banco1.dividendo(3.2)
usuario6 = ContaCorrente(304, 100)
usuario6.debita(70)
print('\nSaldo após pagamento de dividendo da Conta Coupança: {}'.format(usuario6.get_saldo()))
