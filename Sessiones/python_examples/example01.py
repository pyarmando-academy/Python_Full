notas_mayores = 0
notas_menores = 0
i=1
while i<=10:
    nota_act = float(input(f"Ingresar nota {i} "))
    if nota_act >=10.5:
        notas_mayores += 1
    else:
        notas_menores += 1
    i=i+1

print(f"La Cantidad de notas mayores a 10 {notas_mayores}")
print(f"la Cantidad de notas menores a 10 {notas_menores}")







#for x in range(1,10):
#    nota = int(input("Ingresa la Nota:"))




