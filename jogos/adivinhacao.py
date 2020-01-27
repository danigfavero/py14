# Exercício 3.12 - if

# inicializa variáveis
numero = 42
chute = input('Digite um número: ')
chute = int(chute) # transforma a string em int

# verifica chute
if chute == numero:
    print('Você acertou')
else:
    print('Você errou')    


#####################################################

# Inserindo o elif

chute = int(input('Digite um número: '))

# verifica chute
if chute == numero:
    print('Você acertou')
elif chute > numero:
    print('Você errou, seu chute foi maior que o número secreto')
elif chute < numero:
    print('Você errou, seu chute foi menor que o número secreto')

#####################################################

# Refatorando!

chute = int(input('Digite um número: '))

acertou = (chute == numero)
maior = (chute > numero)
menor = (chute < numero)

if acertou:
    print('Você acertou')
elif maior:
    print('Você errou, seu chute foi maior que o número secreto')
elif menor:
    print('Você errou, seu chute foi menor que o número secreto')



