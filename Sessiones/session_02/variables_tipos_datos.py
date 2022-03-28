edad = 28  # todo int
sueldo = 1900.90  # todo float
nombre = "Armando Ruiz"  # todo str
estado = True  # todo bool

# todo variables de tipo de coleccion
lista_personas = [12, True, 'Pedro', 1200.89]  # todo list
sueldo_personas = (1200, 1800, 1900)  # todo tuple inmutables
codigo_personas = {'codigo': 'a100', 'nombre': 'Armando'}  # todo dict mutable
edades_personas = {50, 67, 78, 18}  # todo sets

"""
print(type(lista_personas))
print(type(sueldo_personas))
print(type(codigo_personas))
print(type(edades_personas))
"""

# todo declarnando multiples variabes en una sola linea
first_name, last_name, country = 'Armando', 'Ruiz', 'Perú'

"""
# ?-------------------- Operadores Matematicos--------------------------------
# todo Operadores Matematicos
print(2 + 2)
print(4 * 8)
# todo Division decimal
print(5 / 3)
print(5 // 3)
# todo Residuo de la division
print(23 % 2)
"""

# todo calcular el area de un circulo

"""
radio = 10
area = 3.14 * radio ** 2
print(" El Area de un circulo es:" + str(area))
"""

# todo cast conversion de tipo de datos
# - str() convierte a cadena
# - int() convierte a numerico entero
# - float() convierte a numerico pero con decimal
# - bool() convierte a logico

"""
# todo calcular el peso de un objeto
masa = 75
gravedad = 9.81
peso = masa * gravedad
print("El Peso es:", peso)
"""

#todo convertir soles a dolares

"""
soles =1000
dolar= 3.78
dolares = soles / dolar
print("El Valor en dolares {}".format(dolares))
"""

"""
#todo calcular la edad de una persona
actual = 2022
nacimiento = 1975
edad = actual - nacimiento
print(f'Tu edad es {edad}')
"""

"""
este cs un comentario en 
varias lineas
"""

"""
#todo me permite visualizar las palabras reservada que tiene python
import keyword
print(keyword.kwlist)
"""

"""
 %s string
 %d integer
 %f float
"""
mentor = "Armando"
curso = "Python"
edad = 43
salario = 1700.293344


#print("El Salario con dos decimales es %.1f" %salario)
#print ("%s tiene %d" %(mentor,edad))

#todo entrada de datos
pago_hora=20
nom_emp = input("Ingrese el nombre del empleado:")
horas_trab = int(input("Ingrese las Horas Trabajadas:"))
pago_jornal = horas_trab * pago_hora
print(f'{nom_emp} Recibira de jornal el valor de {pago_jornal}')

#print(type(horas_trab))

