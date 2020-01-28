"""Exercícios 8.12 - Orientação a Objetos
"""

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True


if __name__ == "__main__":

    # testando criação da conta
    conta1 = Conta('123-4', 'João', 200.0, 1000.0)
    conta2 = Conta('123-5', 'Maria', 450.0, 1000.0)
    conta1.extrato()
    conta2.extrato()
    print('')

    # testando saque e depósito
    conta1.saca(200.0)
    conta2.deposita(100.0)
    conta1.extrato()
    conta2.extrato()
    print('')

    # testando tranferência
    if not conta1.transfere_para(conta2, 10.0):
        print('Não foi possível realizar a tranferência')
    if conta2.transfere_para(conta1, 20.0):
        print('Tranferência realizada com sucesso!')
    conta1.extrato()
    conta2.extrato()