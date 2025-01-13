"""Você está recebendo um arquivo contendo 10.000 números inteiros,
um em cada linha. Utilizando lambdas e high order functions, apresente
os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:

map
filter
sorted
sum

Seu código deverá exibir na saída
(simplesmente utilizando 2 comandos `print()`):

a lista dos 5 maiores números pares em ordem decrescente;

a soma destes valores."""

with open('number.txt', 'r') as arquivo:
    numbers = arquivo.readlines()
    number = list(map(lambda value: int(value.strip()), numbers))


pares = list(filter(lambda value: value % 2 == 0, number))

cinco_maiores = lambda list: sorted(list, reverse=True)[:5]

print(cinco_maiores(pares))

soma = sum(cinco_maiores(pares))
print(soma)
