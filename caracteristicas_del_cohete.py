import variables

class caracteristicas_del_cohete():

    def descripcion(self):
        print("")
        print("------------//---------------")
        print("")
        print("creando nave...")
        print("")
        print("digite el nombre de la nave: ")
        variables.nombre=input()
        print("digite el primer color de la nave: ",variables.nombre)
        variables.color1= input()
        print("digite el segundo color de la nave: ",variables.nombre)
        variables.color2 = input()
        print("digite el largo de la nave: ",variables.nombre)
        variables.largo = input()
        print("digite el ancho de la nave: ",variables.nombre)
        variables.ancho = input()
        print("digite el peso de la nave: ",variables.nombre)
        variables.peso = input()
        print("digite el numero de pasajeros de la nave: ",variables.nombre)
        variables.numero_de_pasajeros = input()
        print("--------------//------------------")
        print("")
        print("se a creado una nueva nave")
        print("el nombre de la nave es: ",variables.nombre)
        print("los colores de la nave",variables.nombre, " son: ", variables.color1, " y ", variables.color2)
        print("el largo de la nave",variables.nombre, " es: ", variables.largo, " metros y el ancho es: ", variables.ancho, " metros")
        print("la nave",variables.nombre, " pesa: ", variables.peso, " kilogramos")
        print("la nave",variables.nombre, " tiene una capacidad de: ",variables.numero_de_pasajeros," pasajeros")







