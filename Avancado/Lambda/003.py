"""
Desenvolva uma calculadora rudimentar onde o usuário deve informar:
    qual operação ele deseja realizar
    quais os valores para a realização do cálculo (apenas dois valores)
    e o resultado da operação
"""

OPCOES = {
    "Soma": lambda x, y: x + y,
    "Subtração": lambda x, y: x - y,
    "Multiplicação": lambda x, y: x * y,
    "Divisão": lambda x, y: x / y,
    "Potenciação": lambda x, y: x ** y
}

OPCOES_VALIDAS = {0, 1, 2, 3, 4, 5}

def ler_escolha() -> int:
    return int(input("\nDigite sua escolha (0 para sair): "))

def validar_resultado(escolha: int, num1: float, num2: float) -> float:
    """
    Valida o resultado, chamando a função de acordo com a escolha passada.

    Args:
        escolha: A escolha das opções de 1-5.
        num1: O primeiro número da operação.
        num2: O segundo número da operação.

    Returns:
        O resultado da operação.
    """

    resultado: float = 0

    match escolha:
        case 1:
            resultado = OPCOES["Soma"](num1, num2)
        case 2:
            resultado = OPCOES["Subtração"](num1, num2)
        case 3:
            resultado = OPCOES["Multiplicação"](num1, num2)
        case 4:
            if num2 == 0:
                raise ZeroDivisionError()
            else:
                resultado = OPCOES["Divisão"](num1, num2)
        case 5:
            resultado = OPCOES["Potenciação"](num1, num2)

    return resultado

def main() -> None:
    while True:
        print()
        for i, opcao in enumerate(OPCOES):
            print(f"{i+1}. {opcao}")

        escolha = ler_escolha()

        if escolha not in OPCOES_VALIDAS:
            print("\nOpção inválida.")
            continue

        if escolha == 0:
            break

        try:
            num1 = float(input("\nPrimeiro número: "))
            num2 = float(input("Segundo número: "))

            resultado: float = validar_resultado(escolha, num1, num2)

            print(f"\nO resultado é: {resultado}")

        except ZeroDivisionError:
            print("\nImpossivel dividir por 0.")

if __name__ == "__main__":
    main()
