""" Exercícios 12.6 - Interfaces e classes abstratas
"""
import abc
from cliente import Cliente
from historico import Historico


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
        self._saldo += valor
        self._historico.transacoes.append(f"depósito de {valor}")

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append(f"saque de {valor}")
            return True

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



class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01
   


class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3



class ContaInvestimento(Conta):
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def get_valor_imposto(self):
        return self._saldo * 0.03



class SeguroDeVida:

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05
