"""Exercícios 9.5 - Métodos de classe
"""
from cliente import Cliente
from historico import Historico

class Conta:

    identificador = 1 # variável de classe

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico() 
        # liga uma conta à sua identificação:
        self.identificador = Conta.identificador
        Conta.identificador += 1

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

    def extrato(self):
        print("***EXTRATO***")
        print(f"titular: {self._titular.nome} {self._titular.sobrenome}")
        print(f"cpf: {self._titular.cpf}")
        print(f"numero: {self._numero} \nsaldo: {self._saldo}\n")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True


if __name__ == "__main__":

    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    cliente3 = Cliente('Maria', 'Costa', '333333333-33')
    conta1 = Conta('123-4', cliente1, 1000.0)
    conta2 = Conta('123-5', cliente2, 1000.0)
    conta3 = Conta('123-6', cliente3, 1000.0)
    
    print("***CONTAS CRIADAS***")
    print(conta1.identificador, ":\t", conta1)
    print(conta2.identificador, ":\t", conta2)
    print(conta3.identificador, ":\t", conta3)



    