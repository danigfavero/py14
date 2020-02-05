"""Exercícios 11.7 - Herança e polimorfismo
"""
from cliente import Cliente
from historico import Historico


class Conta:

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

    def __str__(self): # melhoramos o método "extrato" com um método mágico
        extrato = ('Conta: {} \tSaldo : {} \nTitular: {} {} \nCPF: {}'.format(
            self._numero, self._saldo, self._titular.nome,
            self._titular.sobrenome, self._titular.cpf))
        return extrato


    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True
    
    def atualiza(self, taxa): # aplica taxa sobre saldo
        self._saldo += self._saldo * taxa



class ContaCorrente(Conta): # herda da classe Conta

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10    



class ContaPoupanca(Conta): # também herda da classe Conta

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3



if __name__ == "__main__":

    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    cliente3 = Cliente('Maria', 'Costa', '333333333-33')

    c = Conta('123-4', cliente1, 1000.0)
    cc = ContaCorrente('123-5', cliente2, 1000.0)
    cp = ContaPoupanca('123-6', cliente3, 1000.0)

    # testando nosso método de atualizar contas
    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)

    print("\n***********************************************\n")

    # testando o método mágico "__str__"
    print(c)
    print(cc)
    print(cp)

    