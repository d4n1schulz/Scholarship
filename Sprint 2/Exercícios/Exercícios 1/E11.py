"""Escreva uma função que recebe como parâmetro uma lista e
retorna 3 listas: a lista recebida dividida em 3 partes iguais.
Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""


def division(lista):

    indice = int((len(lista)/3))

    a = lista[0:indice]

    b = lista[int(len(a)):indice*2]

    c = lista[indice*2:indice*3]

    return print(a, b, c)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

division(lista)
