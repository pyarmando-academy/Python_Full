from base_datos import empleados

"""
Indicadore.- Buscar un empleado por codigo y mostrar el area y el sueldo que percibe
"""


def buscar_empleado(bd):
    existe = False
    cod_emp = input("Ingrese el codigo del empleado:")
    for item in bd:
        if cod_emp == item['codigo']:
            print(f"El Sueldo del empleado {item['nombre']} "
                  + f"{item['apellido']} es {item['sueldo']} del area de {item['area']}")
            existe = True
            break
    if existe == False:
        print("El Empleado no existe")


# buscar_empleado(empleados)

"""
Indicadore.- Sumar el sueldo de empleados por Area
"""


def suma_sueldos_area(bd):
    suma_sueldos = 0
    existe = False
    try:
        area_buscar = input("Ingrese el Area a totalizar el sueldo:")
        for item in bd:
            if area_buscar == item['area']:
                suma_sueldos = suma_sueldos + item['sueldo']
                existe = True
        if existe == False:
            print("El Area no existe")
        print(f'El Total de la planilla del Area {area_buscar} es {suma_sueldos}')
    except Exception as err:
        print(f"Ha Ocurrdo un error {err}")


suma_sueldos_area(empleados)
