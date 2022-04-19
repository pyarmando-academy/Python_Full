clientes = []
empleados = list()

frutas = ["banana", "naranja", "mango", "sandia"]

# print(type(frutas))
# print(empleados)
# print(frutas)

# todo mostrar un elemento de la lista
# print(frutas[2]) #todo mango
# todo añadir un elemento a la lista
frutas.append("fresa")
frutas.insert(2, "maracuya")
# todo eliminar elementos de la lista
frutas.pop(2)
frutas.remove("fresa")
# todo modificar un elemto de  lista
frutas[0] = "Platano"
# todo ordenar elementos de la lista
frutas.sort()
# frutas.reverse()
# print(frutas)

# for item in frutas:
#    print(item)


lista_invitados = list()
msj = ""
while True:
    invitado = input("Ingresa el nombre del invitado:")
    lista_invitados.append(invitado)
    msj = input("Desea Agregar otro invitado:")
    if msj.upper() == "N":
        print(lista_invitados)
        break

