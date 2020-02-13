""" Exercícios 13.7 - Exceções
"""
import abc
from cliente import Cliente
from historico import Historico
from tributavel_mixin import TributavelMixIn
from excecoes import SaldoInsuficienteError


class Conta(abc.ABC):

    def __init__(self, numero, cliente, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico() 
        self._tipo = self.__class__.__name__

    @property
    def saldo(self):
        return self._saldo	

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo.')
        else:
            self._saldo += valor   
            self._historico.transacoes.append(f"depósito de {valor}")

    def saca(self, valor):
        if (valor < 0):
            raise ValueError('Você tentou sacar um valor negativo.')
        if (self._saldo < valor):
            raise SaldoInsuficienteError('Saldo insuficiente.')
        self._saldo -= valor
        self._historico.transacoes.append(f"saque de {valor}")

    def __str__(self):
        extrato = ('Conta: {} \tSaldo : {} \nTitular: {} {} \nCPF: {}'.format(
            self._numero, self._saldo, self._titular.nome,
            self._titular.sobrenome, self._titular.cpf))
        extrato += '\nTipo da Conta: {}'.format(self._tipo)
        return extrato

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True
    
    @abc.abstractmethod
    def atualiza():
        pass


class ContaCorrente(Conta, TributavelMixIn):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10    

    def get_valor_imposto(self):
        return self._saldo * 0.01
    
    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor:
            raise SaldoInsuficienteError('Saldo insuficiente.')
        self._saldo -= valor + 0.10




class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo.')
        else:
            self._saldo += valor   



class ContaInvestimento(Conta):
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


class SeguroDeVida(TributavelMixIn):

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)

    valor = -1000
    try:
        cc.saca(valor)
        print('Saque de {} realizado com sucesso'.format(valor))
    except ValueError:
        print('O valor a ser sacado deve ser um número positivo.')

    try:
        cc.deposita(valor)
        print('Depósito de {} realizado com sucesso.'.format(valor))
    except ValueError: # opa, não implementamos no deposita!
        print('O valor a ser depositado deve ser um número positivo.')


    valor = 5000.0
    try:
        cc.saca(valor)
        print('Saque de {} realizado com sucesso.'.format(valor))
    except ValueError:
        print('O valor a ser sacado deve ser um número positivo.')
    except SaldoInsuficienteError: # precisamos checar esse erro também :p
        print('Você não possui saldo suficiente para concluir esta operação.')



