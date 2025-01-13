"""Escreva uma função que recebe uma string de números separados por
vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
A string deve ter valor  '1,3,4,6,10,76' """


def soma_string(string):

    lista = string.split(',')
    cont = 0
    for i in lista:
        cont += int(i)
    return print(cont)


numbers = '1,3,4,6,10,76'

soma_string(numbers)
