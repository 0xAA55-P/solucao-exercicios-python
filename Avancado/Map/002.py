"""
Desenvolva um programa que apresente:
a soma dos valores pares
e dos valores ímpares
da sequência ([21, 5, 34, 8, 16, 7, 3])
"""

def pegar_se_par(numero) -> int:
    """Retorna um número se ele for par

    Args:
        numero: o número a checar

    """
    return numero if numero % 2 == 0 else 0

def pegar_se_impar(numero) -> int:
    """Retorna um número se ele for impar

    Args:
        numero: o número a checar
    """

    return numero if numero % 2 != 0 else 0

def main() -> None:
    numeros: list[int] = [21, 5, 34, 8, 16, 7, 3]

    pares: list[int] = sum(map(pegar_se_par, numeros))
    impares: list[int] = sum(map(pegar_se_impar, numeros))

    print(pares)
    print(impares)

if __name__ == '__main__':
	main()
