#Crear un juego utilizando ciclo for
import random
import time

opciones = ['piedra', 'papel', 'tijera']
    
print("Bienvenido al juego de Piedra, Papel o Tijera!")
    
# Ciclo para jugar varias rondas
for ronda in range(3):  # Jugar 3 rondas

    print(f"\nRonda {ronda + 1}")

    eleccion_usuario = input("Escribe 'piedra', 'papel' o 'tijera': ").lower()
    eleccion_computadora = random.choice(opciones)
        
    print(f"\nTu elección: {eleccion_usuario}")
    time.sleep(1)
    print(f"Elección de la computadora: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
        
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
        (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
        (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
        print("¡Ganaste!")
            
    else:
        print("Perdiste!")

time.sleep(2)    