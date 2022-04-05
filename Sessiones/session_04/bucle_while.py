# i = 0
# while i <= 100: # todo True
#     print(i)
#     i = i + 1

# contrasena = "python"
# cont = 0
# try:
#     usuario = input("Ingrese el usuario:")
#     while True:
#         con = input("Ingrese la contraseña:")
#         if con == contrasena:
#             print(f'Bienvenido al sistema {usuario}')
#             break  # todo True
#         else:
#             con += 1
#             print(f'Contraseña errada , intento {cont}')
#             if cont == 3:
#                 print("Supero los intentos , vuelva a intentarlo dentro de 24 horas")
#                 break
# except Exception as error:
#     print(f'Existe un error del codigo {error} ')

import random
numero_azar = random.randint(1,100)
intentos =0
while True:
    numero = int(input("Cual es el numero secreto:?"))
    intentos +=1
    if numero == numero_azar:
        print("Acertastes!!!")
        print(f'Numero de Intentos {intentos}')
        break
    else:
        if numero_azar>numero:
            print(f'El Numero secreto es mayor {numero}')
        else:
            print(f'El Numero secreto es menor que {numero}')


