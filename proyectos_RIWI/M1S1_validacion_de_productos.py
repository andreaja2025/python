# Entrenamiento Módulo 1 – Semana 1
# Sistema de validación de productos
# ANDREA ARIAS-RIWI

# Mensaje de bienvenida
print("=" * 70)
print("Bienvenidos a la Tienda Tecnológica RIWI".center(70))
print("=" * 70)
print("*" * 70)

nombre_de_usuario=input("¿Cómo prefieres ser llamadx?: ")

print(nombre_de_usuario + " sigue las instrucciones para recibir la cotización de tu compra")

# Ingreso de datos
nombre_del_producto = input("Ingrese el nombre del producto: ")
print("Ingrese el precio unitario del producto sin puntos ni comas:")
precio_unitario = input()
print("Ingrese cantidad de productos adquiridos sin puntos ni comas:")
cantidad_de_productos = input()

# Validación: que el precio y la cantidad sean números positivos
if precio_unitario.isdigit() and cantidad_de_productos.isdigit():
    #.isdigit() permite evaluar si todos los caracteres son numeros

    # Conversión de datos
    precio_unitario_float = float(precio_unitario)
    cantidad_de_productos_int = int(cantidad_de_productos)

    #Verifica que sean numeros positivos
    if precio_unitario_float > 0 and cantidad_de_productos_int > 0:
        # Cálculo del costo sin descuento
        costo_sin_descuento = precio_unitario_float * cantidad_de_productos_int

        # Validación del descuento:
        print("Ingrese el porcentaje de descuento del producto debe estar entre 0 y 100:")
        valor_de_descuento = input()
        valor_de_descuento = valor_de_descuento.replace('%', '')
        #.replace si la variable contiene el simbolo % lo reemplaza por espacio en blanco

        valor_de_descuento = valor_de_descuento.replace(',', '.')
        #Se reemplaza las , por . para que float lo interprete como decimal correctamente

        #Validar el descuento ingresado:
        if valor_de_descuento.isdecimal:
        #.isdecimal permite el ingreso de porcentajes en decimal 

            valor_de_descuento_float = float(valor_de_descuento)

            # Validación del descuento (es un número y está entre 0 y 100)
            if 0 <= valor_de_descuento_float <= 100:
                calculo_de_descuento = (valor_de_descuento_float / 100) * precio_unitario_float
                descuento_sobre_producto = precio_unitario_float - calculo_de_descuento
                costo_total_con_descuento = descuento_sobre_producto * cantidad_de_productos_int

                print("=" * 70)
                print(f"Producto: {nombre_del_producto}".ljust(35) + f"Costo total: ${costo_total_con_descuento:.2f}".rjust(35))
                print(" " * 70)
                print("¡Gracias por confiar en RIWI!".center(70))
                print("=" * 70)
                print("Apreciamos tu visita, ¡esperamos verte pronto!".center(70))
            else:
                print("Error: el descuento debe estar entre 0 y 100%.")   
        else:
            print("Error: El porcentaje de descuento no es válido")
    else:
        print("Error: El precio y la cantidad de productos deben ser números positivos.")
else:
    print("Error: El precio y la cantidad de productos deben ser números y no contener puntos ni comas.")