"""
Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final.

Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média.

Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO
"""

def ler_notas(notas: list[float]) -> None:
  for i in range(0, 4):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

def calcular_media(notas: list[float]) -> float:
  media: float = 0
  for nota in notas:
    media += nota

  return media / len(notas)

def main() -> None:
  notas: list[float] = []

  ler_notas(notas)
  media: float = calcular_media(notas)

  if media >= 7:
    print("Aprovado.")
  else:
    notas.append(float(input("Nota da prova final: ")))
    media: float = calcular_media(notas)

    if media >= 5:
      print("Aprovado")
    else:
      print("Reprovado")

if __name__ == '__main__':
	main()
