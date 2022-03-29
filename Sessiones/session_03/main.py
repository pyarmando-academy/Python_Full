from servicios import  *

def menu():
    print("Menu de Opciones")
    print("1:-Lavado")
    print("2:-Alquiler")
    print("3:-Estacionamiento")
    print("4:-Salir")
    ser=int(input("Ingrese el Servicio a solicitar:"))
    if ser == 1:
        print(lavado())
    elif ser ==2:
        print(alquiler())
    elif ser ==3:
        estacionamiento()
    else:
        print(print("Fin del menu"))


menu()




