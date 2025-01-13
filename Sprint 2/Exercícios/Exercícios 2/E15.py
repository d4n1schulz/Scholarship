"""Implemente duas classes, Pato e Pardal , que herdam de uma superclasse
chamada Passaro as habilidades de voar e emitir som.

Contudo, tanto Pato quanto Pardal devem emitir sons diferentes
(de maneira escrita) no console, conforme o modelo a seguir.

Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu"""


class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voando(self):
        print('Voando...')

    def emite_som(self):
        print(f'{self.nome} emitindo som...')


class Pato(Passaro):
    def som(self):
        print('Quack Quack')


class Pardal(Passaro):
    def som(self):
        print('Piu Piu')


pato = Pato('Pato')
pardal = Pardal('Pardal')

print('Pato')
pato.voando()
pato.emite_som()
pato.som()
print('Pardal')
pardal.voando()
pardal.emite_som()
pardal.som()
