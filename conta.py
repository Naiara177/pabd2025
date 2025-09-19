class conta:
    def __init__(self, titular, agencia, numero, pix, saldo):
        self.titular = titular
        self.agencia = agencia
        self.numero = numero
        self.pix = pix
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
    def saca(self, valor):
        self.saldo -= valor
def extrato(self):
        print(f'Titular: {self.titular}')
        print(f'Agencia: {self.agencia}')
        print(f'Numero: {self.numero}')
        print(f'Pix: {self.pix}')
        print(f'Saldo: {self.saldo:.2f}')


def saca(self, valor):
    if self.saldo < valor:
        return False
    else:
        self.saldo -= valor
        return True
    
def deposita(self, valor):
    self.saldo += valor
    return True     



def transfere(self, destino, valor):
    if self.saca(valor):
        destino.deposita(valor)
        return True
    else:
        return False
from conta import Conta


