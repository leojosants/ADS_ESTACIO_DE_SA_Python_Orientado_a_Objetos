import datetime
from extrato2 import Extrato


class Conta:

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["DEPÓSITO", valor, "DATA", datetime.datetime.today()])
        return f'Depósito realizado no valor de R$ {valor}!'

    def sacar(self, valor):
        if self.saldo < valor:
            return f'Saldo suficiente? {False} - Saque não realizado!'
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, "DATA", datetime.datetime.today()])
            return f'Saldo suficiente? {True} - Saque realizado no valor de R${valor}!'

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return 'Saldo insuficiente!'
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["TRANSFERÊNCIA", valor, "DATA", datetime.datetime.today()])
            return f'Transferência realizada para a conta: {conta_destino} no valor: R$ {valor}!'

    def gerar_saldo(self):
        print(
            f'IMPRIMIR SALDO --> Número da conta: {self.numero} | Saldo: R$ {self.saldo}')