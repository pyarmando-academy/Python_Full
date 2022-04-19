class Animal:
    # todo constructor
    def __init__(self, nombre, edad, pelaje=""):
        self.nombre = nombre
        self.edad = edad
        self.pelaje = pelaje

    def __str__(self):
        return f'Mi Animal {self.nombre} tiene {self.edad} Años y tiene su pelaje {self.pelaje}'

    def mensaje(self):
        if self.edad > "50":
            msj = "El Animal es Mayor"
        else:
            msj = "El Animal es Menor"
        return msj

 # todo objetos que se instancia de la clase animal

perro = Animal("Pancho", "4 años")
gato = Animal("Paco", "3 Años")
raton = Animal("Micky", "60 Años", "Plomo")

print(perro.mensaje())

# print(perro.edad)
# print(gato.nombre)
# print(raton.pelaje)
# print(perro.__dict__)
# print(gato.__dict__)
# print(raton.__dict__)
