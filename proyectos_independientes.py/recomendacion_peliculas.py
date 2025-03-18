# programa que recomiende una película basada en la edad del usuario y sus
# preferencias (acción, comedia, terror, etc.). Si el usuario es menor de 13 años, evita
# recomendar películas con clasificación para adultos.

import random

# Mensaje de bienvenida
print("=" * 60)
print("Bienvenidos a la plataforma de streaming superlegal.com".center(60))
print("=" * 60)
print(" " * 60)

print("Ingrese su usuario, si quiere crear uno nuevo escriba: nuevo ")
pedir_usuario= input(">>>>>   ")

#Aqui asocio y almaceno usuarios con sus contraseñas
usuario_y_contraseña= {
    "admin":"cocacolita2",
    "Prueba":"1234"
}

#Aqui asocio y almaceno varias peliculas para adultos a diferentes generos
categoria_peliculas_adultos = {
    "comedia": ["La vida de Brian", "Superbad", "Dos tontos en fuga"],
    "terror": ["El conjuro", "It", "Halloween"],
    "fantasia": ["El señor de los anillos", "Harry Potter y el prisionero de Azkaban", "Pan's Labyrinth"],
    "drama": ["Forrest Gump", "El Padrino", "La lista de Schindler"],
    "acción": ["Mad Max: Furia en la carretera", "John Wick", "Gladiador"],
    "romántica": ["El diario de una pasión", "Titanic", "Antes del amanecer"],
    "ciencia_ficción": ["Blade Runner 2049", "Interstellar", "Matrix"],
    "aventura": ["Indiana Jones", "Piratas del Caribe", "Jurassic Park"],
    "misterio": ["El sexto sentido", "Zodiac", "Seven"],
}

#Aqui asocio y almaceno varias peliculas para niños a diferentes generos
categoria_peliculas_ninos = {
    "comedia": ["Toy Story", "Mi villano favorito", "Madagascar"],
    "aventura": ["Las crónicas de Narnia", "Peter Pan", "Aladdin"],
    "animación": ["El rey león", "Buscando a Nemo", "Kung Fu Panda"],
    "fantasía": ["Harry Potter y la piedra filosofal", "Alicia en el país de las maravillas"],
    "ciencia_ficción": ["WALL-E", "El planeta del tesoro", "Los Mitchell contra las máquinas"],
    "musical": ["Frozen", "Moana", "La Bella y la Bestia"],
    "drama": ["Mi vecino Totoro", "Up", "El viaje de Chihiro"],
    "acción": ["Los Increíbles", "Spider-Man: Un nuevo universo", "Big Hero 6"],
    "misterio": ["Scooby-Doo", "Detective Pikachu", "La casa del reloj en la pared"],
    "romántica": ["Enredados", "La princesa y el sapo", "Cenicienta"]
}

#verifica si el usuario está en la lista donde se almacena usuarios y contraseñas
if pedir_usuario in usuario_y_contraseña:
    pedir_contraseña = input("Ingrese su contraseña: ") 

    #Verifica si la contraseña ingresada es la asociada al usuario
    if pedir_contraseña == usuario_y_contraseña[pedir_usuario]:

        #Decoracion
        print("" * 60)
        print("=" * 22, "SESIÓN INICIADA".center(10), "=" * 22)
        print("" * 60)
        print("¡Bienvenidx!", pedir_usuario, "estamos felices que vuelvas a conectarte")
        print("Queremos recomendarte peliculas que sabemos vas a disfrutar")
        print("pero, antes verificaremos tu edad.")

        edad_del_usuario=input("Ingrese su edad (solo numero): ")
        edad_del_usuario_int = int(edad_del_usuario) #Convertir str a entero
        
        # verifica si el usuario es mayor a 13
        if edad_del_usuario_int > 13:
            print("accediste al perfil", pedir_usuario )
            print("¿De qué género quieres la pelicula?")
            genero_de_pelicula = input(">>>>>   ")
            
            def categoria(seleccion):
                match seleccion:
                    case "comedia":
                        pelicula_random = random.choice(categoria_peliculas_adultos["comedia"])
                        #random.choice escoge aleatoriamente una pelicula del genero comedia
                        print( "Te recomendamos ver" , pelicula_random)
                        
                    case "terror":
                        pelicula_random = random.choice(categoria_peliculas_adultos["terror"])
                        print( "Te recomendamos ver" , pelicula_random)
                        
                    case "fantasia":
                        pelicula_random = random.choice(categoria_peliculas_adultos["fantasia"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "drama":
                        pelicula_random = random.choice(categoria_peliculas_adultos["drama"])
                        print("Te recomendamos ver" , pelicula_random)

                    case "acción":
                        pelicula_random = random.choice(categoria_peliculas_adultos["acción"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "romántica":
                        pelicula_random = random.choice(categoria_peliculas_adultos["romántica"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "ciencia_ficción":
                        pelicula_random = random.choice(categoria_peliculas_adultos["ciencia_ficción"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "aventura":
                        pelicula_random = random.choice(categoria_peliculas_adultos["aventura"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "misterio":
                        pelicula_random = random.choice(categoria_peliculas_adultos["misterio"])
                        print("Te recomendamos ver", pelicula_random)

                    case _:
                        print("Categoría no reconocida. Intenta de nuevo.")            

            #Decoración
            print("*" * 60)
            categoria(genero_de_pelicula)
            #Llama la función categoria y compara con la entrada del usuario almacenada en genero_de_pelicula
            print("🍿 Dale play a la película y disfruta el momento! 🎬✨".center(60))
            #.center centra le texto
            print("*" * 60)

        # verifica si el usuario es menor a 13                                                                    
        elif edad_del_usuario_int <= 13:
            print(pedir_usuario, "accediste al perfil niños")
            print("¿De qué género quieres la pelicula?")
            genero_de_pelicula = input(">>>>>   ")

            def categoria(seleccion):
                match seleccion:
                    case "comedia":
                        pelicula_random = random.choice(categoria_peliculas_ninos["comedia"])
                        print( "Te recomendamos ver" , pelicula_random)
                        
                    case "aventura":
                        pelicula_random = random.choice(categoria_peliculas_ninos["aventura"])
                        print( "Te recomendamos ver" , pelicula_random)
                        
                    case "animación":
                        pelicula_random = random.choice(categoria_peliculas_ninos["animación"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "fantasía":
                        pelicula_random = random.choice(categoria_peliculas_ninos["fantasía"])
                        print("Te recomendamos ver" , pelicula_random)

                    case "ciencia_ficción":
                        pelicula_random = random.choice(categoria_peliculas_ninos["ciencia_ficción"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "musical":
                        pelicula_random = random.choice(categoria_peliculas_ninos["musical"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "drama":
                        pelicula_random = random.choice(categoria_peliculas_ninos["drama"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "acción":
                        pelicula_random = random.choice(categoria_peliculas_ninos["acción"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case "misterio":
                        pelicula_random = random.choice(categoria_peliculas_ninos["misterio"])
                        print("Te recomendamos ver", pelicula_random)

                    case "romántica":
                        pelicula_random = random.choice(categoria_peliculas_ninos["romántica"])
                        print("Te recomendamos ver" , pelicula_random)
                    
                    case _:
                        print("Categoría no reconocida. Intenta de nuevo.")

    else:
        print(" ⚠️ contraseña incorrecta ⚠️")        

elif pedir_usuario == "nuevo":
    print("Establezca su nombre de usuario: ")
    nuevo_usuario= input()

    if nuevo_usuario in usuario_y_contraseña:
        print("⚠️ Ese usuario ya existe. Intenta con otro nombre.")

    else:
        print("Establezca su contraseña: ")
        nueva_contraseña= input()
        usuario_y_contraseña[nuevo_usuario] = nueva_contraseña
        print("Usuario creado correctamente")
        print(usuario_y_contraseña)

else:
    print ("⚠️ Usuario no encontrado, porfavor vuelva a intentar o cree uno nuevo ⚠️")