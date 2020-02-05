"""Exercícios 9.5 - Modificadores de acesso
"""
from cliente import Cliente
from historico import Historico

class Conta:

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico() 

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

    cliente1 = Cliente('João', 'Silva', '123.456.789-00')
    conta1 = Conta('123-4', cliente1, 200.0, 1000.0)

    print("saldo atual: ", conta1.saldo) # 200.0
    conta1.tipo = "Corrente" # AttributeError
    # o slots não permite criar um novo atributo
    