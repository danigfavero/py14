"""Exercícios 11.9 - Classes abstratas
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
        self._tipo = self.__class__.__name__ # tipo da conta

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
        # imprime também o tipo da conta
        extrato += '\nTipo da Conta: {}'.format(self._tipo)
        return extrato


    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True
    
    # torna-se método abstrato:
    @abc.abstractmethod
    def atualiza():
        pass



class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10    



class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3



class ContaInvestimento(Conta):
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5



if __name__ == "__main__":

    # verificando o tipo da conta
    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    cliente3 = Cliente('Maria', 'Costa', '333333333-33')

    conta1 = ContaCorrente('123-4', cliente1, 1000.0)
    conta2 = ContaPoupanca('123-5', cliente2, 1000.0)
    conta3 = ContaInvestimento('123-6', cliente3, 1000.0)

    print(conta1)
    print(conta2)
    print(conta3)


    