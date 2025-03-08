import random
import time
import os
import names

qtd_nomes_unicos = 39080
qtd_nomes_aleatorios = 10000000

random.seed(40)

aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios')

dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

file_path = os.path.join(os.path.dirname(__file__), 'nomes_aleatorios.txt')
with open(file_path, 'w') as file:
    for nome in dados:
        file.write(nome + '\n')
