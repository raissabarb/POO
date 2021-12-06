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
        return print('Conta {}: saldo = {}'.format(self.numero, self.saldo))


class ContaPoupanca(Conta):
    def __init__(self, a, juros):
        super(ContaPoupanca, self).__init__(a)
        self.juros = juros/100

    def get_saldo(self):
        novo_saldo = super().get_saldo()
        novo_saldo += novo_saldo*self.juros
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
            print('O valor de R${} foi creditado com sucesso!\n'.format(quantia))
        else:
            valor_estourado = quantia - val_limite
            print('Não foi possível fazer a operação! Limite estourado em R${}!\n'.format(valor_estourado))

    def imprime(self):
        super().imprime()


raissa = ContaCorrente(245, 500)
saldo = float(input('Digite o saldo: '))
raissa.saldo = saldo
print('Saldo: {}'.format(raissa.saldo))