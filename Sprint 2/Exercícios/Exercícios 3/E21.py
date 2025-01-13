"""Utilizando high order functions, implemente o corpo da função conta_vogais.
O parâmetro de entrada será uma string e o resultado deverá ser a contagem de
vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:

len

filter

lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código."""

def conta_vogais(texto:str)-> int: 
    vogais = ['a', 'e' , 'i', 'o', 'u']
    
    cont_vogais = filter(lambda char: char.lower() in vogais, texto)
    return int(len(list(cont_vogais)))

texto  = 'Daniel'

print(conta_vogais(texto))