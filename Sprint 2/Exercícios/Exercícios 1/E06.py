"""Implemente a função my_map(list, f) que recebe uma lista como
primeiro argumento e uma função como segundo argumento. Esta função
aplica a função recebida para cada elemento da lista recebida e retorna
o resultado em uma nova lista.

Teste sua função com a lista de entrada
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma
função que potência de 2 para cada elemento."""

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(num):
    return num**2


def my_map(list, f):
    new = []
    for i in list:
        new.append(f(i))
    return print(new)


my_map(dados, square)
