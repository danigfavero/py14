# Mini Sistema de Sorteio
Obrigada ao aluno que fez a [primeira implementação](https://gist.github.com/MrCl0wnLab/4fa85ed4b890fe86c284b8d405632d9d)  desse exercício! 

**Conhecimentos necessários:** orientação a objetos básica, arquivos csv, métodos estáticos (decorator), as bibliotecas `random` e `datetime`.

Dado um arquivo _csv_ com nome, cpf e nascimento de algumas pessoas; cadastre tickets para depois sortear 10 delas aleatoriamente.

## Implementação

1. `dados_sorteio.csv`  
    Esse arquivo é dado pelo usuário. Contém nome, cpf e nascimento de algumas pessoas. Está no formato _comma separated values_. No [gist](https://gist.github.com/danigfavero/608f71546a937a0d3f29fad215282d39) com a resposta, tem um arquivo pronto para teste.

2. `pessoa.py`  
    Deverá conter a classe `Pessoa`, que guardará todos os dados pessoais do candidato ao sorteio, além de calcular sua idade e verificar se é maior de idade. Guarde essas informações em atributos.

3. `cadastro.py`  
    Será responsável por cadastrar o ticket de uma `Pessoa`. O número do ticket será dado pelas seguintes operações:
    
    - Obtenha o `id()` do objeto que guarda o cpf da pessoa
    - Embaralhe a ordem dos números desse id

4. `main.py`  
    Esse arquivo será responsável por ler o _csv_, criar uma `Pessoa` pra cada linha do _csv_ e cadastrar um ticket pra cada pessoa que for maior de idade. Depois de cadastrados, sorteie 10 tickets e imprima os vencedores.

## Dicas
1. Crie classes para implementar comportamentos e entidades no seu sistema.
2. Faça testes. Bons testes exploram todas as possibilidades: como seu programa lida com menores de idade cadastrados?
3. Depois que seu código funcionar, tente refatorá-lo! Você está escrevendo muitas vezes uma mesma linha de código? Lembre-se que esse pode ser um mau sinal. Revise algumas estruturas de repetição e encapsulamento.
4. Documente. Deixe bem claro pro usuário o que cada classe/método recebe e devolve. Não se preocupe em especificar _como_ você implementou, somente _o que_ aquele bloco de código faz.

A minha implementação está [neste gist](https://gist.github.com/danigfavero/608f71546a937a0d3f29fad215282d39). Tente fazer antes de olhar a resposta!