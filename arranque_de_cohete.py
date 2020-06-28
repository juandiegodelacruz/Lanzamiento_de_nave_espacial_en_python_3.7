import time

import variables



class arranque_de_cohete():
    def conteo_re(self):

        print("oprima cualquier tecla para continuar con el despegue de la nave",variables.nombre)
        input()
        print("despegue de la nave: ",variables.nombre)
        for i in range(0,10):
            print(10-i,"...")
            time.sleep(1)
        print("injection de la nave: ",variables.nombre)

    def despegar(self):

        for i in range (1,10):

            cohete="""
                       / \\
                      /   \\
                     /_____\\
                     ¦space¦
                     ¦_____¦
                     ¦     ¦
                     ¦cohe2¦
                     ¦_____¦"""
            capsula = """
                       / \\
                      /   \\
                     /_____\\
                     ¦     ¦
                     ¦space¦
                     ¦_____¦
                     """
            if i <= 5:
                print(cohete,variables.nombre,i*20," kilometros de altura")
            else:
                print(capsula,variables.nombre, i * 20, " kilometros de altura")

            if i == 5:
                print("")
                print("separacion del cohete secundario")
                print("")
            time.sleep(2)
        print("")
        print("        capsula",variables.nombre,"en órbita")
        print("")
        print("--------------//------------------")
        print("")

