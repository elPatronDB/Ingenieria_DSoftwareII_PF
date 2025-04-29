import sys
import random

def comparar_jugada(humano, programa):
    if humano == programa:
        return 0
    elif (humano == "piedra" and programa == "tijera") or \
        (humano == "papel" and programa == "piedra") or \
        (humano == "tijera" and programa == "papel"):
        return 1
    else:
        return -1

def main():
    if len(sys.argv) != 4:
        print("Uso: python juego.py <opcion1> <opcion2> <opcion3>")
        print("Opciones válidas: piedra, papel, tijera")
        sys.exit(1)

    opciones_validas = ["piedra", "papel", "tijera"]
    # Convertir las jugadas a minúsculas
    jugadas_humano = [arg.lower() for arg in sys.argv[1:]]
    
    for jugada in jugadas_humano:
        if jugada not in opciones_validas:
            print(f"Error: '{jugada}' no es una opción válida. Usa: piedra, papel, tijera")
            sys.exit(1)

    jugadas_programa = [random.choice(opciones_validas) for _ in range(3)]
    
    puntos_humano = 0
    puntos_programa = 0
    
    for i in range(3):
        resultado = comparar_jugada(jugadas_humano[i], jugadas_programa[i])
        print(f"Ronda {i+1}: Humano ({jugadas_humano[i]}) vs Programa ({jugadas_programa[i]})")
        if resultado == 1:
            puntos_humano += 1
            print("  Gana humano")
        elif resultado == -1:
            puntos_programa += 1
            print("  Gana programa")
        else:
            print("  Empate")

    print(f"\nJugadas del programa: {' '.join(jugadas_programa)}")
    print(f"Puntaje final: Humano {puntos_humano} - Programa {puntos_programa}")
    
    if puntos_humano > puntos_programa:
        print("Ganador final: Humano")
    elif puntos_programa > puntos_humano:
        print("Ganador final: Programa")
    else:
        print("Empate final")

if __name__ == "__main__":
    main()