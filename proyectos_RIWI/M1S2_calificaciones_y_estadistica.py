## Entrenamiento Módulo 1 – Semana 2
## Sistema 
#ANDREA ARIAS-RIWI

import time
#Libreria de la cual se importa time.sleep para generar un retardo

import re
# "re" Es una librería de Python que se implementa para buscar patrones dentro de cadenas de texto. 
# se implementa .search porque permite encontrar la primera coincidencia del patrón 
# en la cadena sin necesidad de que esté al inicio, lo cual me da mayor flexibilidad 
# y facilita el flujo del programa.
# Así, se puede verificar si existe un patrón dentro de un texto sin necesidad de hacer
# una comprobación manual o iterativa.

#Mensaje de bienvenida
#Con el objetivo de mejorar la experiencia del usuario
print("=" * 66)
print("Centro de entrenamiento RIWI".center(66))
print("=" * 66)
print("*" * 66)

print(" " * 66)
print("¡Hola Team lider!".center(66))
      
nombre_usuario = input("¿Cómo quieres ser llamadx?: ")
salir = "sesion iniciada"
    
while salir != "salir" :
    print("=" * 66)
    print("MENÚ PRINCIPAL".center(66))
    print("=" * 66)
    print(" " * 66)
    
    print( nombre_usuario + " tienes habilitado el ingreso de notas del grupo Ciénaga")
    mensaje_opciones= print("ingresa el numero de la opcion a ejecutar: ")
    print("1 -> Ingresar una calificacion 2 -> Ingresar varias calificaciones")
    servicio_escogido= input()
    
    match servicio_escogido:
        # Paso 1: Solicita al usuario ingresar una calificación numérica
        case "1":
            print("Ingresa una calificación, debe estar entre 0 y 100: ")
            print("*En RIWI se considera aprobado con calificacion de 70*")

            calificacion_ingresada =input()
    
            # Validar la calificación numérica 
            if calificacion_ingresada.isnumeric():
                #isnumeric() permite evaluar si el contenido de la vaiable son solo numeros
        
                calificacion_ingresada_float = float(calificacion_ingresada) #conversion de str a float
                
                # determinar el estado de aprobación según la calificación
                if calificacion_ingresada_float >=70 and calificacion_ingresada_float <=100:
                    print("*" * 66)
                    print(f"La calificación del coder es: {calificacion_ingresada_float}".ljust(32) + f" Estado: Aprobado".rjust(32))
                    print("*" * 66)
                    print()    
                    print("Actividad finalizada, si desea cerrar sesión ingrese ' salir '")
                    print("si no, dar enter")
                    salir = input()
                
                    if salir.lower() == 'salir':
                        print("Saliendo del programa...")
                        time.sleep(2) # retardo de 2 segundos
        
                elif calificacion_ingresada_float >=0 and calificacion_ingresada_float <=69:
                    print("*" * 66)
                    print(f"La calificación del coder es: {calificacion_ingresada_float}".ljust(31) + f" Estado: Reprobado".rjust(31))
                    #.ljust justifica el texto y variable a la izquierda
                    #.rjust justifica el texto a la derecha

                    #Pregunta de control para finalizar la sesion, si no, va al menu
                    print("*" * 66)
                    print() 
                    print("Actividad finalizada, si desea cerrar sesión ingrese ' salir '")
                    print("si no, dar enter")
                    salir = input()
                
                    if salir.lower() == 'salir':
                        print("Saliendo del programa...")
                        time.sleep(2) # retardo de 2 segundos
                else:
                    print("Error: La calificacion debe estar entre 0 y 100")    
            else:
                print("Error: la calificación debe estar en el rango de 0 a 100")
        
        case "2":
            
            # Paso 2: Permite al usuario ingresar una lista de calificaciones
            print(nombre_usuario + " ingresa la lista de calificaciones separadas por coma ' , ' ")
            print("La calificación debe estar entre 0 y 100:")
            
            calificaciones_ingresadas = input()
                       
            # Validar la calificación numérica (se debe permitir que contenga ' , ' y ' . ' )
            if re.search(r'^(\d+(\.\d+)?)(,\s*\d+(\.\d+)?)*$', calificaciones_ingresadas):
                # re.search() busca en la variable si contiene un patron definido
                # el patron que se define asegura que toda la cadena consista únicamente en números y comas,
                # y permite números decimales al permitir un punto seguido de dígitos
                # Los espacios después de las comas son permitidos gracias a \s*,
                # que acepta cualquier cantidad de espacios en blanco (incluso ninguno).
                # Esta validación también puede realizarse con un ciclo for
                
                # Divide la cadena por comas y guarda las calificaciones en una lista.
                lista_calificaciones = calificaciones_ingresadas.split(",")
                
                # Elimina los espacios alrededor de cada calificación.
                calificaciones = [cal.strip() for cal in lista_calificaciones]

                # Convierte las calificaciones a float.
                calificaciones = [float(cal) for cal in calificaciones]
                
                # Inicia el ciclo con indice en 0
                indice = 0

                while indice < len(calificaciones):
                    # len() me permite saber la longitud de la lista
                    # Continúa mientras el índice sea menor que la longitud de la lista

                    # Verifica si la calificación está fuera del rango
                    if calificaciones[indice] < 0 or calificaciones[indice] > 100:
                        # indice esta dentro de corchetes y como una variable
                        # que va incrementando, permitiendo recorrer los elementos de la lista
                        #empieza en cero que corresponde a la posición 1
                        
                        print(" " * 60)
                        #Si la condicion se cumple, muestra error
                        print(f"Error: La calificación {calificaciones[indice]} no está en el rango de 0 a 100.")

                        #Pregunta de control, para dar la opcion de finalizar la sesion
                        print() 
                        print("*" * 60)
                        print("Actividad finalizada, si desea cerrar sesión ingrese ' salir '")
                        print("si no, dar enter")
                        salir = input()
                
                        if salir.lower() == 'salir':
                            print("Saliendo del programa...")
                            time.sleep(2) # retardo de 2 segundos

                        #Si el usuario no termina la sesion, lo lleva al menu
                    indice += 1 # Incrementa el índice para revisar la siguiente calificación                

                else:                      
                    # Calcular el promedio de las calificaciones
                    promedio = sum(calificaciones) / len(calificaciones)
                    #len se usa para obtener la cantidad de elementos en la lista de calificaciones
                    # para poder obtener el numero de calificaciones y utilizarlo como divisor
                
                    # Mostrar el promedio calculado
                    print(f"El promedio de las calificaciones es: {promedio:.2f}")
                
                    # Paso 3: Utilizar un ciclo while para contar las calificaciones mayores que el valor especificado
                    valor_comparacion = input("Ingresa un valor para comparar las calificaciones: ")
                    valor_comparacion_float = float (valor_comparacion)
                
                    # Inicializar el contador que llevará la cuenta de las calificaciones mayores
                    # que el valor de comparación
                    contador_mayores = 0

                    # Inicializar el índice en 0 para empezar desde el primer elemento de la lista
                    # de calificaciones
                    indice = 0

                    # Ciclo que recorrerá toda la lista de calificaciones
                    while indice < len(calificaciones):
                        # Verificar si la calificación en la posición actual (índice) es mayor
                        # que el valor de comparación
                        if calificaciones[indice] > valor_comparacion_float:
                            # Si la condición se cumple, incrementar el contador de calificaciones mayores
                            contador_mayores += 1

                        # Avanzar al siguiente índice de la lista para revisar la siguiente calificación
                        indice += 1

                    # Al finalizar el ciclo, 'contador_mayores' tendrá la cantidad total de calificaciones
                    # mayores que el valor de comparación
                                
                    # Paso 4: Mostrar cuántas calificaciones son mayores que el valor especificado
                    print(f"Hay {contador_mayores} calificaciones mayores que {valor_comparacion}.")
                
                    # Paso 4: Contar cuántas veces aparece una calificación específica
                    calificacion_especifica = input("Ingresa una calificación específica para contar cuántas veces aparece: ")
                    calificacion_especifica_float = float(calificacion_especifica)
                
                    # Inicializar el contador de apariciones
                    contador_apariciones = 0

                    # Usar un ciclo for para contar las apariciones de la calificación específica
                    for calificacion in calificaciones:
                    
                        # Si la calificación no es igual a la calificación específica, continuar con la siguiente iteración
                        if calificacion != calificacion_especifica_float:
                            continue
                        
                        # Aumentar el contador cada vez que encontramos la calificación específica
                        contador_apariciones += 1
                                               
                    # Mostrar cuántas veces aparece la calificación específica
                    print(f"La calificación {calificacion_especifica} aparece {contador_apariciones} veces en la lista.")

                    print() 
                    print("*" * 66)
                    print("Actividad finalizada, si desea cerrar sesión ingrese ' salir '")
                    print("si no, dar enter")
                    salir = input()
                
                    if salir.lower() == 'salir':
                        print("Saliendo del programa...")
                        time.sleep(2) # retardo de 2 segundos                          
            else:
                print("Las calificaciones no deben contener caracteres diferente a los permitidos")                          
print("Sesión cerrada")