paises = {"colombia": "bogota", "chile": "santiago", "uruguay": "montevideo"}
# print(paises)
"""
print(paises["colombia"])
print(paises["chile"])
print(paises["uruguay"])
"""

# todo el tamaño de un diccionario
# print(len(paises))
# print(type(paises))

# todo añadir elementos al diccionario
# todo los diccionarios son un tipo de coleccion que son INMUTABLES
paises["venezuela"] = "caracas"
# todo eliminar elementos del diccionario
paises.pop("chile")
# todo modificar un elemento del diccionario
paises["venezuela"] = "merida"
paises["venezuela"] = "caracas"
# print(paises)

# TIPO DATOS JSON
clientes = [
    {'cuenta': '234567', 'apellido': 'Ruiz', 'nombre': 'Armando', 'saldo': 70000},
    {'cuenta': '234568', 'apellido': 'Gomez', 'nombre': 'Raul', 'saldo': 75000},
    {'cuenta': '234569', 'apellido': 'Tapia', 'nombre': 'Omar', 'saldo': 10000},
    {'cuenta': '234510', 'apellido': 'Cespedes', 'nombre': 'Pedro', 'saldo': 60000},
    {'cuenta': '234511', 'apellido': 'Gonzales', 'nombre': 'Maria', 'saldo': 90000},
]

cuenta = input("Ingrese el Numero de cuenta:")
for item in clientes:
    if (cuenta == item["cuenta"]):
        print(f' {item["nombre"]} {item["apellido"]} tu saldo actual es {item["saldo"]}')
        break
