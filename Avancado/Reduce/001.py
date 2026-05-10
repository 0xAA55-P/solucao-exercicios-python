"""
Desenvolva um programa que apresente o maior e o menor valores da sequência ([54, 10, 29, 87, 7, 64])
"""

from functools import reduce

numeros: list[int] = [ 54, 10, 29, 87, 7, 64 ]

menor: int = reduce(lambda x, y: x if x < y else y, numeros)
maior: int = reduce(lambda x, y: x if x > y else y, numeros)

print(menor)
print(maior)
