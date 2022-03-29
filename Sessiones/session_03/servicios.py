def lavado():
    tipolavado = input("Ingrese el tipo de lavado:")
    if tipolavado == "rapido":
        precio = 5
    elif tipolavado == "profundo":
        precio = 10
    else:
        return "No Existe ese tipo de lavado"
    impuesto = precio * 0.12
    total = precio + impuesto
    return f' el total a pagar es {total}'


def alquiler():
    tauto = input("Ingresar el tipo de auto:")
    dias = int(input("Ingresar el Numero de dias:"))
    if tauto == "A":
        precio = 100
    elif tauto == "B":
        precio = 150
    elif tauto == "C":
        precio = 200
    else:
        return "No existe ese tipo de auto"
    subtotal = dias * precio
    impuesto = subtotal * 0.12
    total = subtotal + impuesto
    return f' el total a pagar es {total}'


def estacionamiento():
    horas = int(input("ingrese la cantidad de horas:"))
    if horas <= 3:
        tarifa = 2.00
    elif horas >= 4:
        tarifa = (horas * 0.50) + 2.00
        if tarifa > 10: tarifa = 10
    return f' el total a pagar es {tarifa}'
