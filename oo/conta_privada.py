"""Exercícios 9.5 - Modificadores de acesso
"""
from cliente import Cliente
from historico import Historico

class Conta:

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        # todos os atributos privados
        self.__numero = numero
        self.__titular = cliente
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = Historico() 

    def deposita(self, valor):
        self.__saldo += valor
        self.__historico.transacoes.append(f"depósito de {valor}")

    def saca(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            self.__historico.transacoes.append(f"saque de {valor}")
            return True

    def extrato(self):
        print("***EXTRATO***")
        print(f"titular: {self.__titular.nome} {self.__titular.sobrenome}")
        print(f"cpf: {self.__titular.cpf}")
        print(f"numero: {self.__numero} \nsaldo: {self.__saldo}\n")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True


if __name__ == "__main__":

    cliente1 = Cliente('João', 'Silva', '123.456.789-00')
    conta1 = Conta('123-4', cliente1, 200.0, 1000.0)

    print(conta1._Conta__numero) # 123-4
    print(conta1.__numero) # AttributeError


# "conta1._Conta__numero" não é uma boa prática, queríamos que o atributo
# fosse privado.
    