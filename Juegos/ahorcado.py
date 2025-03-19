import random
#Juego del ahorcado utilizando ciclo for

palabra = "yoongi"
letras_adivinadas = ["_"] * len(palabra)
intentos = 7

print("¡Bienvenido al juego del Ahorcado!")
print("La palabra tiene", len(palabra), "letras.")
    
for intento in range(intentos):
    print("Palabra:", " ".join(letras_adivinadas))
    letra = input("Adivina una letra: ").lower()

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                    letras_adivinadas[i] = letra
        print("¡Bien hecho! La letra está en la palabra.")

    else:
        print("¡Que mal! La letra no está en la palabra.")
        
    if "_" not in letras_adivinadas:
        print("¡Felicidades! Has adivinado la palabra:", palabra)
        break
else:
    print("¡Se acabaron los intentos! La palabra era:", palabra)
