class Familia:
    def __init__(self, padre, madre, hijos=[]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        cadena = f'{self.padre}  {self.madre}'
        for hijos in self.hijos:
            cadena = cadena + ' '+  f'{hijos}'
        return cadena


Familia_Gomez = Familia("Juan", "Teresa", ["Pepe", "Julia"])
Familia_Perez = Familia("Pedro", "Manuela", ['Jaimito', 'Arturito','Jorge'])

print(Familia_Perez)
