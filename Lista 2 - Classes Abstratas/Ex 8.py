from abc import ABC, abstractmethod


class RoboAbs(ABC):

    nome = ''
    posicaoXAtual = 0
    posicaoYAtual = 0
    direcao = 0

    def __init__(self):
        pass

    @abstractmethod
    def move(self, passos):
        pass


class RoboAbstrato(RoboAbs):
    def __init__(self, n, px, py, d):
        super(RoboAbstrato, self).__init__()
        self.nome = n
        self.posicaoXAtual = px
        self.posicaoYAtual = py
        self.direcao = d
        self.passos = 0

    def move(self, passos):
        self.passos = passos
        return self.passos

    def moveX(self, passos):
        self.posicaoXAtual += passos
        return self.posicaoXAtual

    def moveY(self, passos):
        self.posicaoYAtual += passos
        return self.posicaoYAtual

    def mudaDirecao(self, novaDir):
        self.direcao = novaDir
        return self.direcao

    def direcaoAtual(self):
        return self.direcao

    def toString(self):
        resultado = 'Nome do robô: {}\nPosição do robô: ({}, {})\nDireção do robô: {}'.format(self.nome, self.posicaoXAtual, self.posicaoYAtual, self.direcao)
        return resultado


class RoboSimples(RoboAbstrato):
    def __init__(self, n, px, py, d):
        super(RoboSimples, self).__init__(n, px, py, d)

    def move(self, passos):
        if self.direcaoAtual() == 0:
            self.moveX(passos)
        elif self.direcaoAtual() == 90:
            self.moveY(passos)
        elif self.direcaoAtual() == 180:
            self.moveX(-passos)
        elif self.direcaoAtual() == 270:
            self.moveY(-passos)

    def mudaDirecao(self, novaDir):
        self.direcao = super().mudaDirecao(novaDir)
        return self.direcao

    def direcaoAtual(self):
        dirOutraClasse = super().direcaoAtual()
        if dirOutraClasse < 45 or dirOutraClasse >= 315:
            self.direcao = 0
        elif (dirOutraClasse >= 45) and (dirOutraClasse < 135):
            self.direcao = 90
        elif (dirOutraClasse >= 135) and (dirOutraClasse < 225):
            self.direcao = 180
        elif (dirOutraClasse >= 225) and (dirOutraClasse < 315):
            self.direcao = 270
        return self.direcao


class RoboABateria(RoboAbstrato):
    def __init__(self, n, px, py, d, e):
        super(RoboABateria, self).__init__(n, px, py, d)
        self.energia = e
        self.energiaASerGasta = 0

    def moveX(self, passos):
        super().moveX(passos)

    def moveY(self, passos):
        super().moveY(passos)

    def mudaDirecao(self, novaDir):
        return super().mudaDirecao(novaDir)

    def move(self, passos):
        self.energiaASerGasta = passos * 10
        if self.energiaASerGasta <= self.energia:
            if self.direcaoAtual() == 0:
                self.moveX(passos)
            elif self.direcaoAtual() == 45:
                self.energiaASerGasta = passos * 14
                self.moveX(passos)
                self.moveY(passos)
            elif self.direcaoAtual() == 90:
                self.moveY(passos)
            elif self.direcaoAtual() == 135:
                self.energiaASerGasta = passos * 14
                self.moveX(passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 180:
                self.moveX(-passos)
            elif self.direcaoAtual() == 225:
                self.energiaASerGasta = passos * 14
                self.moveX(-passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 270:
                self.moveY(-passos)
            elif self.direcaoAtual() == 315:
                self.energiaASerGasta = passos * 14
                self.moveX(-passos)
                self.moveX(passos)
            self.energia -= self.energiaASerGasta

    def toString(self):
        resultado = super().toString() + '\nEnergia do robô: {}'.format(self.energia)
        return resultado

    def recarrega(self, energia):
        self.energia += energia
        return self.energia


class RoboComMemoria(RoboAbstrato):
    def __init__(self, n, px, py, d):
        super(RoboComMemoria, self).__init__(n, px, py, d)
        self.totPassosN = 0
        self.totPassosS = 0
        self.totPassosL = 0
        self.totPassosO = 0

    def moveX(self, passos):
        if passos > 0:
            self.totPassosL += passos
        else:
            self.totPassosO += passos
        super().moveX(passos)

    def moveY(self, passos):
        if passos > 0:
            self.totPassosN += passos
        else:
            self.totPassosS += passos
        super().moveY(passos)

    def mudaDirecao(self, novaDir):
        super().mudaDirecao(novaDir)

    def retornaAOrigem(self):
        origemX = self.posicaoXAtual - self.totPassosL
        origemY = self.posicaoYAtual - self.totPassosN
        return print('Ponto de origem: ({}, {})'.format(origemX, origemY))


class RoboPesadoABateria(RoboABateria):
    def __init__(self, n, px, py, d, e, peso):
        super(RoboPesadoABateria, self).__init__(n, px, py, d, e)
        self.peso = peso

    def moveX(self, passos):
        return super().moveX(passos)

    def moveY(self, passos):
        return super().moveY(passos)

    def toString(self):
        return super().toString()

    def recarrega(self, energia):
        return super().recarrega(energia)

    def mudaDirecao(self, novaDir):
        return super().mudaDirecao(novaDir)

    def move(self, passos):
        if self.energiaASerGasta <= self.energia:
            if self.direcaoAtual() == 0:
                self.energiaASerGasta = passos * self.peso
                self.moveX(passos)
            elif self.direcaoAtual() == 45:
                self.energiaASerGasta = passos * self.peso * 1.4
                self.moveX(passos)
                self.moveY(passos)
            elif self.direcaoAtual() == 90:
                self.energiaASerGasta = passos * self.peso
                self.moveY(passos)
            elif self.direcaoAtual() == 135:
                self.energiaASerGasta = passos * self.peso * 1.4
                self.moveX(passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 180:
                self.energiaASerGasta = passos * self.peso
                self.moveX(-passos)
            elif self.direcaoAtual() == 225:
                self.energiaASerGasta = passos * self.peso * 1.4
                self.moveX(-passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 270:
                self.energiaASerGasta = passos * self.peso
                self.moveY(-passos)
            elif self.direcaoAtual() == 315:
                self.energiaASerGasta = passos * self.peso * 1.4
                self.moveX(-passos)
                self.moveX(passos)
            self.energia -= self.energiaASerGasta


class RoboQueDeveVoltar(RoboABateria):
    def __init__(self, n, px, py, d, e):
        super(RoboQueDeveVoltar, self).__init__(n, px, py, d, e)
        self.totPassosN = 0
        self.totPassosS = 0
        self.totPassosL = 0
        self.totPassosO = 0
        self.totX = 0
        self.totY = 0
        self.xini = px
        self.yini = py

    def moveX(self, passos):
        if passos > 0:
            self.totPassosL += passos
        else:
            self.totPassosO += passos
        super().moveX(passos)

    def moveY(self, passos):
        if passos > 0:
            self.totPassosN += passos
        else:
            self.totPassosS += passos
        super().moveY(passos)

    def mudaDirecao(self, novaDir):
        return super().mudaDirecao(novaDir)

    def totx(self):
        self.totX = self.totPassosL + self.totPassosO
        return self.totX

    def toty(self):
        self.totY = self.totPassosN + self.totPassosS
        return self.totY

    def posX(self):
        return self.posicaoXAtual

    def posY(self):
        return self.posicaoYAtual

    def voltarAOrigemRapido(self, cont):
        if cont > self.energia:
            return print('Você está no início novamente!')
        else:
            return print('Não é possível voltar ao início. Energia insuficiente!')

    def move(self, passos):
        self.energiaASerGasta = passos * 10
        if self.energiaASerGasta <= self.energia:
            if self.direcaoAtual() == 0:
                self.moveX(passos)
            elif self.direcaoAtual() == 45:
                self.energiaASerGasta = passos * 14
                self.moveX(passos)
                self.moveY(passos)
            elif self.direcaoAtual() == 90:
                self.moveY(passos)
            elif self.direcaoAtual() == 135:
                self.energiaASerGasta = passos * 14
                self.moveX(passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 180:
                self.moveX(-passos)
            elif self.direcaoAtual() == 225:
                self.energiaASerGasta = passos * 14
                self.moveX(-passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 270:
                self.moveY(-passos)
            elif self.direcaoAtual() == 315:
                self.energiaASerGasta = passos * 14
                self.moveX(-passos)
                self.moveX(passos)
            self.energia -= self.energiaASerGasta
        return self.energiaASerGasta


# Ex 1
r = RoboABateria('C3PO', 45, 45, 90, 100)
r.move(3)
print(r.direcaoAtual())
print(r.energia)
print(r.energiaASerGasta)
r.recarrega(10)
print(r.energia)
print(r.toString())

# Ex 4
print('\n')
r1 = RoboABateria('Wall-e', 30, 50, 135, 50)
r1.move(5)
print(r1.toString())

print('\n')
r2 = RoboAbstrato('R2D2', 20, 30, 45)
r2.mudaDirecao(3)
print(r2.direcaoAtual())

# Ex 5
print('\n')
r3 = RoboSimples('Zeta', 30, 20, 40)
print(r3.direcaoAtual())
r3.mudaDirecao(52)
print(r3.direcaoAtual())

# Ex 6
print('\n')
r4 = RoboComMemoria('Aman', 10, 20, 90)
r4.moveX(20)
r4.retornaAOrigem()
print('Ponto atual: ({}, {})'.format(r4.posicaoXAtual, r4.posicaoYAtual))
r4.moveY(-3)
print('Ponto atual: ({}, {})'.format(r4.posicaoXAtual, r4.posicaoYAtual))
print('Passos N: {}\nPassos S: {}\nPassos L: {}\nPassos O: {}'.format(r4.totPassosN, r4.totPassosS, r4.totPassosL, r4.totPassosO))

# Ex 7
print('\n')
r5 = RoboPesadoABateria('BB-8', 60, 50, 270, 550, 12.5)
print('Ponto atual: ({}, {})'.format(r5.posicaoXAtual, r5.posicaoYAtual))
r5.move(27)
print(r5.toString())

# Ex 8
print('\n')
r6 = RoboQueDeveVoltar('AVA', 30, 45, 180, 500)
r6.move(3)
print(r6.direcaoAtual())
r6.mudaDirecao(45)
r6.move(6)
r6.move(4)
r6.move(-3)
r6.moveX(10)
r6.moveY(2)
print(r6.energia)
print(r6.energiaASerGasta)
r6.recarrega(10)
print(r6.energia)
print(r6.toString())
print('Passos N: {}\nPassos S: {}\nPassos L: {}\nPassos O: {}'.format(r6.totPassosN, r6.totPassosS, r6.totPassosL, r6.totPassosO))
print(r6.move(6))  # contabiliza a energia gasta por essa quantidade de movimento
print(r6.energia)  # energia atual
contx = r6.totx()
conty = r6.toty()
cont = contx + conty
print(r6.xini, r6.yini)  # posição inicial
print(r6.posX(), r6.posY())
r6.voltarAOrigemRapido(r6.move(cont))
print('Posição: ({}, {})'.format(r6.xini, r6.yini))