"""Verifique se cada uma das palavras da lista
['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

É necessário que você imprima no console exatamente assim:

A palavra: maça não é um palíndromo
A palavra: arara é um palíndromo
A palavra: audio não é um palíndromo
A palavra: radio não é um palíndromo
A palavra: radar é um palíndromo
A palavra: moto não é um palíndromo
"""

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in palavras:
    if i[::-1] == i:
        print(f'A palavra: {i} é um palíndromo')
    else:
        print(f'A palavra: {i} não é um palíndromo')
