# 3.13 while
numero = 42
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número: '))

    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if acertou:
        print('Você acertou')
        break
    elif maior:
        print('Você errou, seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou, seu chute foi menor que o número secreto')
    rodada = rodada + 1

# 3.15 for

numero = 42
tentativas = 3

for rodada in range(1, tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número: '))

    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if acertou:
        print('Você acertou')
        break
    elif maior:
        print('Você errou, seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou, seu chute foi menor que o número secreto')

