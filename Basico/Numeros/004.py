# Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar

numero = int(input("Número: "))

if numero % 2 == 0:
  print(f"{numero} é par")
else:
  print(f"{numero} é impar")
