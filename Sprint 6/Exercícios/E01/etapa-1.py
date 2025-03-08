import random

random_numbers = [random.randint(0, 1000) for _ in range(250)]

random_numbers.reverse()

print(random_numbers)
