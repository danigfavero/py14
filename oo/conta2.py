"""Exercícios 8.12 - Orientação a Objetos - Opcionais
"""
import datetime
from cliente import Cliente
from historico import * # O asterisco importa todo o código do módulo citado


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = Data(datetime.date.today().day,
                                  datetime.date.today().month,
                                  datetime.date.today().year)
        self.historico = Historico() 

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"depósito de {valor}")

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"saque de {valor}")
            return True

    def extrato(self):
        # modifica extrato pra imprimir dados do cliente
        print("***EXTRATO***")
        print(f"titular: {self.titular.nome} {self.titular.sobrenome}")
        print(f"cpf: {self.titular.cpf}")
        print(f"numero: {self.numero} \nsaldo: {self.saldo}\n")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para\
            conta {destino.numero}")
            return True


if __name__ == "__main__":

    # Testando cliente
    cliente1 = Cliente('João', 'Silva', '123.456.789-00')
    conta1 = Conta('123-4', cliente1, 200.0, 1000.0)
    conta1.extrato()

    cliente2 = Cliente('Maria', 'Fernandes', '123.456.789-01')
    conta2 = Conta('123-5', cliente2, 450.0, 1000.0)
    conta2.extrato()
    # Podemos criar um Cliente sem Conta.
    # Não podemos criar uma Conta sem um Cliente.


    # Testando histórico
    conta1.deposita(100.0)
    conta1.saca(50.0)
    conta1.transfere_para(conta2, 200.0)
    conta1.historico.imprime()



