import time
import variables
class recuperar_cohete():
    def recuperacion(self):
        print("recuperando cohete secundario")
        print("")
        for i in range(1,5):
            cohete2="""
                       _____
                      ¦     ¦
                      ¦cohe2¦
                      ¦_____¦"""
            print(cohete2,100-i*20,"kilometros de altura")
            time.sleep(2)
        print("")
        print("cohete secundario de la nave",variables.nombre,"recuperado")
        print("")