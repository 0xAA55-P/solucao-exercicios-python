"""
Desenvolva um jogo de acerte o número, onde:
    o computador escolhe um número inteiro aleatório de 0 a 10
    e o usuário tem 5 tentativas para adivinhar o número
"""

from random import randint

def aumentar_pontuacao(tentativas: int) -> int:
    """Aumenta a pontuação com base nas tentativas

    Args:
        tentativas: As tentativas antes de acertar

    Returns:
        pontuacao = 100 se tentativas == 5
        pontuacao = 10 se tentativas == 0
        pontuacao = 0 caso nenhum caso acima atenda
    """

    pontuacao: int = 0

    if tentativas == 5:
        pontuacao += 100
    elif tentativas == 0:
        pontuacao += 10

    return pontuacao

def jogo(numero: int) -> None:
    """Inicio do jogo

    Args:
        numero: o número aleatório gerado
    """

    tentativas: int = 5

    fim_por_vitoria: bool = True
    # True: Encerrou o jogo acertando
    # False: Encerrou o jogo por tentativas demais

    while True:
        chute = int(input("Chute: "))
        tentativas -= 1

        if chute > numero:
            print("Muito alto!")
        elif chute < numero:
            print("Muito baixo!")
        else:
            break # acertou

        if tentativas < 0:
            print("Tentativas excedidas!")
            fim_por_vitoria = False
            break

    pontuacao = aumentar_pontuacao(tentativas)

    if fim_por_vitoria:
        print("\nAcertou!")
        print(f"Tentativas: {5 - tentativas}")
        print(f"Pontuação: {pontuacao}\n")

def main() -> None:
    while True:
        try:
            numero: int = randint(0, 10)
            jogo(numero)

            if input("Continuar? (S/N): ").strip().upper() == "N":
                break

        except ValueError:
            print("\nValor inválido!\n")

        except KeyboardInterrupt:
            print("\nFim da partida.\n")
            break

if __name__ == "__main__":
    main()
