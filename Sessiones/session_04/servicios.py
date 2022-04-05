def lavado():
    tipolavado = input("Ingrese el tipo de lavado:")
    if tipolavado == "rapido":
        precio = 5
    elif tipolavado == "profundo":
        precio = 10
    else:
        return "No existe el tipo de lavado"
    impuesto = precio * 0.12
    total = precio + impuesto
    return f' El Total a pagar es {total}'


def alquiler():
    tauto = input("Ingresar el Tipo de Auto:")
    dias = int(input("Ingresar el Numero de Dias:"))
    if tauto == "A":
        precio = 100
    elif tauto == "B":
        precio = 150
    elif tauto == "C":
        precio = 200
    else:
        return "No Existe este tipo de Auto"
    subtotal = dias * precio
    impuesto = subtotal * 0.12
    total = subtotal + impuesto
    return f'El Total a pagar es {total}'


def estacionamiento():
    horas = int(input("Ingrese la cantidad de horas:"))
    if horas <= 3:
        tarifa = 2.00
    elif horas >= 4:
        tarifa = (horas * 0.50) + 2.00
        if tarifa > 10: tarifa = 10
    return f'El Total a pagar es {tarifa}'


def menu():
    while True:
            print("Menu de Opciones")
            print("1:-Lavado")
            print("2:-Alquiler")
            print("3:-Estacionamiento")
            print("4.-Salir")
            ser = int(input("Ingrese el servicio a solicitar:"))
            if ser == 1:
                print(lavado())
            elif ser == 2:
                print(alquiler())
            elif ser == 3:
                print(estacionamiento())
            else:
                print("Fin del Menu")
            respta = input("Desea Continuar:<s/n>")
            if respta == "N":
                break
