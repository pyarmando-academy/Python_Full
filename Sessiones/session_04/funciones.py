def mifuncion():
    print("Esto es una funcion en PYTHON")

def suma(a,b):
    res = a + b
    print(res)

def mensaje(nombre,msj="Adios"):
    saludo = msj + " " +nombre
    print(saludo)

def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

def calculo(a,b):
    suma = a + b
    return suma

print(calculo(23,45))

#nombres=["Juan","Pedro","Raul"]

#listar_nombres(nombres)

