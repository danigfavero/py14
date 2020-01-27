# 3.9 if
numero = 42
chute = input('Digite um número: ')
chute = int(chute) # 3.10 str->int

if chute == numero:
    print('Voce acertou')
else:
    print('Você errou')    

# 3.11 elif
chute = int(input('Digite um número: '))

if chute == numero:
    print('Voce acertou')
elif chute > numero:
    print('Você errou, seu chute foi maior que o número secreto')
elif chute < numero:
    print('Você errou, seu chute foi menor que o número secreto')

# Refatorando!
chute = int(input('Digite um número: '))

acertou = chute == numero
maior = chute > numero
menor = chute < numero

if acertou:
    print('Você acertou')
elif maior:
    print('Você errou, seu chute foi maior que o número secreto')
elif menor:
    print('Você errou, seu chute foi menor que o número secreto')



