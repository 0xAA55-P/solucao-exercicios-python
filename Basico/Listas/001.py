# Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

def main() -> None:
  notas: list[float] = []

  for i in range(0, 4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

  maior: float = notas[0]
  menor: float = notas[0]
  media: float = 0

  for nota in notas:
    # obs; tambem existe as funções max(notas) e min(notas) para descobrir o maior e o menor valor da lista
    if nota > maior:
      maior = nota

    if nota < menor:
      menor = nota

    media += nota

  media /= len(notas)

  print(f"Maior: {maior} | Menor: {menor} | Média: {media:.2f}")

if __name__ == '__main__':
	main()
