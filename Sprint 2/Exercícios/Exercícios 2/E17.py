"""Exercícios Parte 2
Crie uma classe  Calculo  que contenha um método que aceita
dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe,
implemente um método de subtração, que aceita dois parâmetros, X e Y,
e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1"""


class Calculo:
    def __init__(self):
        self.x = None
        self.y = None

    def soma(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    def subtracao(self, x, y):
        self.x = x
        self.y = y
        return self.x - self.y


x = 4
y = 5

calculo = Calculo()

print(f'Somando: 4 + 5 = {calculo.soma(4, 5)}')
print(f'Subtraindo: 4 - 5 = {calculo.subtracao(4, 5)}')
