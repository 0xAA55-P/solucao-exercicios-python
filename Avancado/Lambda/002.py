# Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar

numero = int(input("Número: "))

check_par_impar = lambda numero: print("Par") if numero % 2 == 0 else print("Impar")

check_par_impar(numero)
