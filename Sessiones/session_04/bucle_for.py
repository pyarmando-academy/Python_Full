# for x in range(10):
#     if x == 5:
#         #todo salir del bucle
#         break
#     else:
#         print(x,"Hola Mundo")

#
# for y in range (1,10,2):
#     print(y)


# cursos =["PYTHON","FLASK","DJANGO","IA"]
#
# for item in cursos:
#     print(item)

# todo Contadores
# todo Acumuladores

# c = 0
# sum = 0
# for item in range(5):
#     notas = float(input(f'Ingresa la Nota {item}:'))
#     c += 1
#     sum += notas
# prom = sum / c
# if prom >= 10.5:
#     msj = "El Alumno Aprobo la materia"
# else:
#     msj = "El Alumno desaprobo la materia"
# print(f'La Cantidad de notas ingresadas {c} y el promedio de notas es {prom}  {msj}')

nomina = 0
for i in range(1, 11):
    sueldo = float(input(f'ingrese el sueldo {i}: $'))
    nomina += sueldo
print('\nLa Nomina que debe pagarse es:$', nomina)
