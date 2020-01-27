# Exercício 3.12 - while

# inicializando variáveis
numero = 42
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    
    # jogando...
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número: '))

    # variáveis booleanas
    acertou = (chute == numero)
    maior = (chute > numero)
    menor = (chute < numero)

    # verifica chute
    if acertou:
        print('Você acertou')
        break # fim do laço!
    elif maior:
        print('Você errou, seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou, seu chute foi menor que o número secreto')

    rodada = rodada + 1 # incrementa rodada!

#############################################################

# Exercício 3.16 - for

# inicializando variáveis
numero = 42
tentativas = 3

for rodada in range(1, tentativas + 1):
    # jogando...
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('Digite um número: '))

    # variáveis booleanas
    acertou = (chute == numero)
    maior = (chute > numero)
    menor = (chute < numero)

    # verifica chute
    if acertou:
        print('Você acertou')
        break # fim do laço!
    elif maior:
        print('Você errou, seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou, seu chute foi menor que o número secreto')

