"""Escreva uma função que recebe um número variável de parâmetros não
nomeados e um número variado de parâmetros nomeados e imprime o
valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)"""


def func(num1, num2, num3, value1, parametro_nomeado='alguma coisa', x=20):
    return print(f'{num1}\n{num2}\n{num3}\n{value1}\n{parametro_nomeado}\n{x}')


func(1, 3, 4, 'hello')
