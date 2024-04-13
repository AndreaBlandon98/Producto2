import random

def generar_numeros():
    return random.randint(0, 100), random.randint(0, 100)

def main():
    num1, num2 = generar_numeros()
    suma_correcta = num1 + num2
    while True:
        respuesta = int(input(f"¿Cuánto es {num1} + {num2}? "))
        if respuesta == suma_correcta:
            print("¡Correcto! Esa es la suma.")
            break
        else:
            print("Esa no es la suma correcta. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
