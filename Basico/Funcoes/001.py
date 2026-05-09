# Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def par_ou_impar(numero: int) -> bool:
  return numero % 2 == 0

def main() -> None:
  numero: int = 42

  if par_ou_impar(numero):
    print(f"{numero} é par")
  else:
    print(f"{numero} é impar")

if __name__ == '__main__':
	main()
