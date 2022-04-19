import csv

def listado_empleados_csv():
    with open('empleados.csv', 'r') as employees:
        leer_archivo = csv.reader(employees)
        empleados = list(leer_archivo)
        return empleados


def empleados_area(data_empleados, areabuscar):
    encontrado = False
    empleados_lista = []
    for codigo, nombre, apellido, sueldo, area, estado, pais in data_empleados:
        if area == areabuscar and estado == "True":
            nombrecompleto = f'{nombre} {apellido}'
            empleados_lista.append((nombrecompleto, sueldo))
            encontrado=True
    if encontrado == False:
        print("No Existe Empleados en esa Area")
        return
    return empleados_lista


area = input("Ingrese el Area a filtra:")
print(empleados_area(listado_empleados_csv(), area))
