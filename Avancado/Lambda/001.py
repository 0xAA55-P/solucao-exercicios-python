# Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes

nome: str = input("Nome completo: ").split()

check_nome = lambda nome: print(nome[0], nome[-1])

check_nome(nome)
