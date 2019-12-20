# 4.5 Exercícios

# E1
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] 

max = lista[0]
for i in lista:
    if i > max:
        max = i
print('Máximo: {}'.format(max))

min = lista[0]
for i in lista:
    if i < min:
        min = i
print('Mínimo: {}'.format(min))

print('Pares:')
for i in lista:
    if i%2 == 0:
        print(i)

primeiro = lista[0]
ocorrencias = 0
for i in lista:
    if i == primeiro:
        ocorrencias += 1
print('O primeiro elemento se repete {} vezes'.format(ocorrencias))

soma = 0
for i in lista:
    soma += i
media = soma/len(lista)
print('Média: {}'.format(media))

negativos = 0
for i in lista:
    if i < 0:
        negativos += i
print('Soma dos elementos negativos: {}'.format(negativos))

# E2 
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
idade = int(input('Idade: '))
lista = [nome, sobrenome, idade]
for i in lista:
    print(i)

# E3
notas = []
soma = 0
for i in range(4):
    nota = int(input('Insira a nota:'))
    notas.append(nota)
    soma += nota
print('Notas:')
for i in notas:
    print(i)
media = soma/len(notas)
print('Média: {}'.format(media))

# E4
pessoa = {}
nome = input('Nome: ')
pessoa['nome'] = nome
idade = int(input('Idade: '))
pessoa['idade'] = idade
cidade = input('Cidade: ')
pessoa['cidade'] = cidade
for key in pessoa.keys():
    print('{}: {}'.format(key, pessoa[key]))

# E5
lista = [pessoa]
pergunta = input('Quer adicionar uma nova pessoa (S/N)? ')
if 'N'.upper() in pergunta.upper():
    criando = False
criando = True

while criando:
    pessoa = {}
    nome = input('Nome: ')
    pessoa['nome'] = nome
    idade = int(input('Idade: '))
    pessoa['idade'] = idade
    cidade = input('Cidade: ')
    pessoa['cidade'] = cidade

    lista.append(pessoa)
    pergunta = input('Quer continuar adicionar uma nova pessoa? (S/N)')
    if 'N'.upper() in pergunta.upper():
        criando = False
    criando = True
for i in lista:
    print('Outra pessoa...')
    for key in lista[key].keys():
        print('{}: {}'.format(key, pessoa[key]))   
