import os
import sys
import random
import time

def limpiarPantalla():
    try:
        if 'TERM' not in os.environ:
            os.environ['TERM'] = 'xterm'
        
        if sys.platform.startswith('win'):
            _ = os.system('cls')
        else:
            _ = os.system('clear')
    except Exception:
        print('\n' * 50)

def compararJugada(humano, programa):
    humano = humano.lower()
    programa = programa.lower()
    
    if humano == programa:
        return 0
    elif (humano == "piedra" and programa == "tijera") or \
         (humano == "papel" and programa == "piedra") or \
         (humano == "tijera" and programa == "papel"):
        return 1
    else:
        return -1

def validarJugada(jugada):
    opcionesValidas = ["piedra", "papel", "tijera"]
    jugada = jugada.lower()
    if jugada not in opcionesValidas:
        limpiarPantalla()
        print(f"Error: '{jugada}' no es una opción válida. Usa: {', '.join(opcionesValidas)}")
        sys.exit(1)
    return jugada

def main():
    limpiarPantalla()
    print("Bienvenido al juego de piedra, papel o tijera")
    if len(sys.argv) != 4:
        print("Instrucciones: Escribe en consola: \n>>> python juego_DB.py op1 op2 op3\n\n***El espacio representa una ronda")
        print("\n*Opciones válidas: piedra, papel, tijera")
        sys.exit(1)

    try:
        jugadasHumano = [validarJugada(arg) for arg in sys.argv[1:]]
    except AttributeError:
        limpiarPantalla()
        print("Únicamente se permite piedra, papel o tijera")
        sys.exit(1)

    print(f"\nTus jugadas: {' '.join(jugadasHumano)}")
    time.sleep(1)

    opcionesValidas = ["piedra", "papel", "tijera"]
    jugadasPrograma = [random.choice(opcionesValidas) for _ in range(3)]
    
    puntosHumano = 0
    puntosPrograma = 0
    
    for i in range(3):
        print(f"\n>>>>>{i+1}: Humano ({jugadasHumano[i]}) vs Programa ({jugadasPrograma[i]})")
        resultado = compararJugada(jugadasHumano[i], jugadasPrograma[i])
        if resultado == 1:
            puntosHumano += 1
            print("        Gana humano")
        elif resultado == -1:
            puntosPrograma += 1
            print("        Gana programa")
        else:
            print("        Empate")
        time.sleep(2)

    print(f"\n****Jugadas del programa: {' '.join(jugadasPrograma)}****")
    print(f"******Puntaje final: Humano {puntosHumano} - Programa {puntosPrograma}*********")
    
    if puntosHumano > puntosPrograma:
        print("Ganador final: Humano")
    elif puntosPrograma > puntosHumano:
        print("Ganador final: Programa")
    else:
        print("Empate final")

if __name__ == "__main__":
    main()