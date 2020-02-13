# Validador de CPF em Python

**Conhecimentos necessários:** variáveis, tipos embutidos, condicionais, laços, listas, funções, exceções.

Faça um programa que recebe uma _string_ da entrada padrão e verifica se é um CPF válido conforme as normas do ministério da fazenda.

## Normas
Suponha o CPF "529.982.247-25".
1. Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente de números de 10 à 2 e soma os resultados. Assim:

        5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2

    O resultado do nosso exemplo é:

        295

    O próximo passo da verificação também é simples, basta multiplicarmos esse resultado por 10 e dividirmos por 11.

        295 * 10 / 11

    O resultado que nos interessa na verdade é o RESTO da divisão. Se ele for igual ao primeiro dígito verificador (primeiro dígito depois do '-'), a primeira parte da validação está correta.

    Observação Importante: Se o resto da divisão for igual a 10, nós o consideramos como 0.

2. A validação do segundo dígito é semelhante à primeira, porém vamos considerar os 9 primeiros dígitos, mais o primeiro dígito verificador, e vamos multiplicar esses 10 números pela sequencia decrescente de 11 a 2. Vejamos:

        5 * 11 + 2 * 10 + 9 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 2 * 5 + 4 * 4 + 7 * 3 + 2 * 2

    O resultado é:

        347

    Seguindo o mesmo processo da primeira verificação, multiplicamos por 10 e dividimos por 11.

        347 * 10 / 11

    Verificando o RESTO, como fizemos anteriormente, temos:

        O resultado da divisão é '315' e o RESTO é 5

    Verificamos, se o resto corresponde ao segundo dígito verificador.

3. CPFs com dígitos repetidos (111.111.111-11, 222.222.222-22, ...) são inválidos.


## Implementação

1. Trate a entrada: para lidar com o CPF, você terá que transformar a string numa lista somente com os numerais do valor inserido. Caracteres como "." e "-" deverão ser ignorados. Além disso, garanta que o CPF tem o formato correto (11 algarismos).

2. Agora que você tem os dígitos, faça as três verificações citadas acima e devolva se o CPF é válido ou não.


## Dicas:

1. Divida cada verificação e formatação da entrada em funções. Lembre-se que encapsulamento facilita a vida de todo mundo :-)
2. Faça testes. Bons testes exploram todas as possibilidades: tente CPFs corretos e incorretos (e tente cada erro separado e combinado: os dois últimos dígitos errados, depois tente com os dígitos repetidos, etc). Não se esqueça dos testes absurdos: "aaaaaaaaaaaaaaaaaaaa" ou "" podem ser entradas de usuário, como o seu programa lida com elas?
3. Depois que seu código funcionar, tente refatorá-lo! Você está escrevendo muitas vezes uma mesma linha de código? Lembre-se que esse pode ser um mau sinal. Revise algumas estruturas de repetição e encapsulamento.
4. Documente. Deixe bem claro pro usuário o que cada função recebe e devolve. Não se preocupe em especificar _como_ você implementou, somente _o que_ a função faz.

A minha implementação está no arquivo _cpf.py_ nesse mesmo diretório. Tente fazer antes de olhar a resposta!