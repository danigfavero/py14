# 5.5 Exercícios - Estruturas de Dados

# Exercício 1 (lista)
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] 

# a) Maior elemento da lista
max = lista[0]
for i in lista:
    if i > max:
        max = i
print('Máximo: {}'.format(max))

# b) Menor elemento da lista
min = lista[0]
for i in lista:
    if i < min:
        min = i
print('Mínimo: {}'.format(min))

# c) Números pares na lista
print('Pares:')
for i in lista:
    if i%2 == 0:
        print(i)

# d) Número de ocorrências do primeiro elemento na lista
primeiro = lista[0]
ocorrencias = 0
for i in lista:
    if i == primeiro:
        ocorrencias += 1
print('O primeiro elemento se repete {} vezes'.format(ocorrencias))

# e) Média dos elementos
soma = 0
for i in lista:
    soma += i
media = soma/len(lista)
print('Média: {}'.format(media))

# f) Soma dos elementos negativos
negativos = 0
for i in lista:
    if i < 0:
        negativos += i
print('Soma dos elementos negativos: {}'.format(negativos))

# Exercício 2 (lista) 
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
idade = int(input('Idade: '))
lista = [nome, sobrenome, idade]
for i in lista:
    print(i)

# Exercício 3 (lista)
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

# Exercício 4 (dicionário)
pessoa = {}
nome = input('Nome: ')
pessoa['nome'] = nome
idade = int(input('Idade: '))
pessoa['idade'] = idade
cidade = input('Cidade: ')
pessoa['cidade'] = cidade
for key in pessoa.keys():
    print('{}: {}'.format(key, pessoa[key]))

# Exercício 5 (estruturas de dados compostas)

# inicializando variáveis (e utilizando o exemplo anterior)
criando = True
lista = [pessoa]
pergunta = input('Quer adicionar uma nova pessoa (S/N)? ')
if 'N'.upper() in pergunta.upper():
    criando = False

while criando:
    # adicionando pessoas à lista
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

# imprimindo de forma "organizada"
for pessoa in lista:
    print('###########################')
    for key in pessoa.keys():
        print('{}:\t{}'.format(key, pessoa[key])) # o '\t' dá um tab!
