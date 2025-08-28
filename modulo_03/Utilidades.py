# main.py
from utilidades import soma, subtracao, potencia

def main():
    print("=== Teste do módulo utilidades ===")
    try:
        a = float(input("Digite A: "))
        b = float(input("Digite B: "))
        e = int(input("Expoente para A**expoente: "))
    except ValueError:
        print("Entrada inválida. Rode novamente e digite números válidos.")
        return

    print(f"{a} + {b} = {soma(a, b)}")
    print(f"{a} - {b} = {subtracao(a, b)}")
    print(f"{a} ** {e} = {potencia(a, e)}")

if __name__ == "__main__":
    main()

