# 3.16 exercícios opcionais
def adivinhacao():
    numero = 42
    pontos = 1000

    nivel = input('Escolha o nível 1, 2 ou 3:')
    if nivel == '1':
        tentativas = 20
    elif nivel == '2':
        tentativas = 10
    elif nivel == '3':
        tentativas = 5        

    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        print('Você tem {} pontos'.format(pontos))
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
        pontos -= abs(numero - chute)

if __name__ == "__main__":
    adivinhacao()