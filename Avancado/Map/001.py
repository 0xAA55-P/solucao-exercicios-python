"""
Desenvolva um programa que converta todas as temperaturas desta lista (°C):
 ([22.5, 40, 13, 29, 34]) para Fahrenheit
"""

def para_fahrenheit(temperatura_celsius: float) -> float:
    """Converte Celsius Para Fahrenheit

    Args:
        temperatura_celsius: A temperatura em celsius

    Returns:
        A temperatura em Fahrenheit

    """

    return (temperatura_celsius * 9 / 5) + 32

def main() -> None:
    celsius: list[float] = [ 22.5, 40, 13, 29, 34 ]

    fahrenheit: list[float] = map(para_fahrenheit, celsius)

    print(list(fahrenheit))

if __name__ == "__main__":
    main()
