# consumo = float(input("Ingrese el monto a consumir:"))
# if consumo <= 100:
#     des = consumo * 0.10
# else:
#     des = consumo * 0.20
# imp = consumo * 0.18
# total = (consumo - des) + imp
# print("El Descuento: {} , El Impuesto {} , El Total {}".format(des,imp,total))




# nota1 = int(input("Ingrese la Nota1:"))
# nota2 = int(input("Ingrese la Nota2:"))
# nota3 = int(input("Ingrese la Nota3:"))
#
# promedio = (nota1 + nota2 + nota3) / 3
#
# if promedio >= 7:
#     print("Promocionado")
# else:
#     if promedio >= 4 and  promedio< 7 :
#         print("Regular")
#     else:
#         print("Reprobado")


# De un operario se conoce su sueldo y los años de antigüedad. Se pide
# confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

sueldo_oper = float(input("Ingrese el sueldo del operario:"))
años_trab= int(input("Ingrese los años del servicios del operario:"))

if sueldo_oper<500 and años_trab>=10:
    print("Se aumenta el 20 $ del sueldo")
    print(f'el nuevo sueldo es {sueldo_oper*0.20+sueldo_oper}')
else:
    if sueldo_oper<500 and años_trab <10:
        print("Se aumenta el 5% del sueldo")
        print(f'El Nuevo Sueldo es {sueldo_oper*0.05+sueldo_oper}')
    else:
        if sueldo_oper>500:
            print("El Sueldo se mantiene sin cambios")
            print(f'El Sueldo actual es{sueldo_oper}')


