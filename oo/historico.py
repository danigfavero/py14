import datetime


class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print(f"{self.dia} de {self.mes}, {self.ano}")


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"data abertura: {self.data_abertura}")
        print("transações: ")
        for t in self.transacoes:
            print("-", t)
