from caracteristicas_del_cohete import *
class crear_cohete(caracteristicas_del_cohete):
        def mostrar_datos():
                caracteristicas = caracteristicas_del_cohete()
                caracteristicas.descripcion()
                input("oprima cualquier tecla para crear el siguinte cohete")
                print("--------------//------------------")
                print("")
                print("se a creado un nuevo cohete")
                print("el nombre del cohete es: ", nombre)
                print("los colores del cohete", nombre, " son: ", color1, " y ", color2)
                print("el largo del cohete", nombre, " es: ", largo, " metros y el ancho es: ", ancho, " metros")
                print("el cohete", nombre, " pesa: ", peso, " kilogramos")
                print("el cohete", nombre, " tiene una capacidad de: ", num_pasajeros, " pasajeros")
