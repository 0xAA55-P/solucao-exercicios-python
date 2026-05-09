# Desenvolva um programa que leia quatro notas e que apresente a média final

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media: float = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Média: {media:.2f}")
