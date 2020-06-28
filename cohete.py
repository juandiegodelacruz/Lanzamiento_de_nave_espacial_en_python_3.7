from caracteristicas_del_cohete import *
from arranque_de_cohete import *
from recuperar_cohete import*

class cohete(recuperar_cohete,arranque_de_cohete,caracteristicas_del_cohete):
    pass

lunar = cohete()

while True:
    pregunta = input("digite c para crear una nave nueva y f para finalizar el programa: ")
    if pregunta=="c":
        lunar.descripcion()
        lunar.conteo_re()
        lunar.despegar()
        lunar.recuperacion()
    else:
        break

