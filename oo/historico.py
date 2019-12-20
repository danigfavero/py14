import datetime
from cliente import *

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print("{} de {}, {}".format(self.dia, self.mes, self.ano))


class Historico:

    def __init__(self):
        self.data_abertura = Data(datetime.date.today().day,
                                  datetime.date.today().month,
                                  datetime.date.today().year)
        self.transacoes = []

    def imprime(self):
        print("data de abertura: ", end="")
        self.data_abertura.imprime()
        print("transações: ")
        for t in self.transacoes:
            print("-", t)

class TributavelMixIn:

    def get_valor_imposto(self):
        pass
