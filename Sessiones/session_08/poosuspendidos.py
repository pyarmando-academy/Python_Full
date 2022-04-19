import csv


class Productos:
    def __init__(self, codigo="", producto="", stock=0, suspendido=""):
        self.codigo = codigo
        self.producto = producto
        self.stock = stock
        self.suspendido = suspendido
        self.productos = []

    def cargar_productos_csv(self):
        with open('inventario.csv', 'r') as data_inventario:
            csv_leer = csv.reader(data_inventario)
            self.productos = list(csv_leer)
            suspendidos = []
            for self.codigo, self.producto, self.stock, self.suspendido in self.productos:
                if self.suspendido == 'SI':
                    suspendidos.append((self.codigo, self.producto, self.suspendido))
            return suspendidos


invent = Productos()
print(invent.cargar_productos_csv())
