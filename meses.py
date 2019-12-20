# 4.2
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

n = 1

while(n < 4):
    mes = input("Escolha um mês (1-12): ")
    if 1 <= mes <= 12:
        # print('O mês é {}'.format(mes[mes-1])) na apostila
        print('O mês é {}'.format(meses[mes-1]))
    n += 1