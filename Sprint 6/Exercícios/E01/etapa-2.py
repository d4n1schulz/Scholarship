import random
import os

animais = ["cachorro", "gato", "elefante", "tigre", "leão", "girafa", "zebra", "macaco", "urso", "lobo",
           "raposa", "coelho", "veado", "canguru", "panda", "leopardo", "guepardo", "hipopótamo", "rinoceronte", "crocodilo"]

animais.sort()

[print(animal) for animal in animais]

file_path = os.path.join(os.path.dirname(__file__), 'animais.txt')

with open(file_path, "w") as file:
    for animal in animais:
        file.write(animal + "\n")