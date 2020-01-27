# Exercício 3.16 - 

# inicializando variáveis
numero = 42
pontos = 1000

# escolha do nível do jogo
nivel = input('Escolha o nível 1, 2 ou 3:')
if nivel == '1':
    tentativas = 20
elif nivel == '2':
    tentativas = 10
elif nivel == '3':
    tentativas = 5     

for rodada in range(1, tentativas + 1):
    
    # jogando...
    print('Tentativa {} de {}'.format(rodada, tentativas))
    print('Você tem {} pontos'.format(pontos))
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

    pontos -= abs(numero - chute) # diminui total de pontos

print("Fim de jogo.")
print("Você fez {}/1000 pontos!".format(pontos))