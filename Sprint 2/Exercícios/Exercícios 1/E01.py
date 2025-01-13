"""Exercícios Parte 1
Dada a seguinte lista:



a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



Faça um programa que gere uma nova lista contendo apenas números ímpares."""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for dado in a:
    if dado % 2 != 0:
        b.append(dado)

print(b)
