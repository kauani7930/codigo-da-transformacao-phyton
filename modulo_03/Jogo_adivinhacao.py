# jogo_adivinhacao.py
import random
import math

def jogar():
    print("=== Jogo de Adivinhação (1 a 100) ===")
    segredo = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Seu palpite: "))
        except ValueError:
            print("Digite um número INTEIRO.")
            continue

        tentativas += 1

        if palpite == segredo:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
            break

        diferenca = abs(segredo - palpite)
        distancia = ("muito longe" if diferenca >= 30
                     else "longe" if diferenca > 10
                     else "perto")

        raiz_aprox = math.isqrt(segredo)
        dica = "maior" if palpite < segredo else "menor"

        print(f"Errou! O número é {dica} que {palpite}. "
              f"Você está {distancia}. (Raiz aprox. do segredo: {raiz_aprox})")

if __name__ == "__main__":
    jogar()
