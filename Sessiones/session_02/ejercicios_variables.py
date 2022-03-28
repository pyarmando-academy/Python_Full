
#print("Resolvere" ,"Ejercicios en PYTHON",sep='*')
#print("PYTHON" ,end="")
#print("Es Facil de aplicar")

#print("Saltos de linea. viene un salto \n\n")
#print("\t lineas Nuevas \n\n")


#pantalones = int(input("Cuantas cantidades de pantalones tienes en stock..?"))
#venta = int(input("¿Cuantas cantidades vendistes en el dia: "))
#print(f'Si comenzastes con {pantalones} y vendistes {venta} , te quedan en stock {pantalones-venta} disponibles')


total_plato = int(input("Total a pagar..?"))
personas = int(input("Entre cuantas personas se dividiran la cuenta..?"))
propina = int(input('Porcentaje de propina mozo(valor numerico..?'))
impuesto = 0.18
porc_propina = propina/100

total_cuenta = print(f'''{'*'*30}
El total de la cuenta es:
Plato:\t\t ${total_plato}
Impuesto: \t {impuesto*100} % (${impuesto*total_plato})
Propina :\t {propina} % (${porc_propina*total_plato})
Total a Pagar.\t $ {total_plato + impuesto*total_plato + porc_propina*total_plato}

Divido en \t\t {personas} Personas
Total por personas:\t ${round(((total_plato + impuesto + porc_propina) /personas),2)}
{'*'*30}
''')
