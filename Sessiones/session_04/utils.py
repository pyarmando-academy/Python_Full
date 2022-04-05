def edad_persona(nac, act=2022):
    edad = act - nac
    return edad


def calcular_mayor(num1, num2):
    if num1 > num2:
        msj = f'El Numero Mayor es {num1}'
    elif num2 > num1:
        msj = f'El Numero Mayot es {num2}'
    else:
        msj = "Los Numeros Son Iguales"
    return msj


def soles_dolares(soles,vd=3.70):
    dolares = soles / vd
    return dolares