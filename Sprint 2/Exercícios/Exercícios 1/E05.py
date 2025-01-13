"""Exercícios Parte 1
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json"""

import json

with open('person.json', encoding='utf-8') as person:
    dados = json.load(person)

print(dados)
