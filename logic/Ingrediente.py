
class Ingrediente:

    def getIngrediente(self):
        return ({self.nombre : self.precio})

    def getPrecio(self):
        return self.precio

    def getNombre(self):
        return self.nombre

    def __init__(self, precio, nombre):
        self.precio = precio
        self.nombre = nombre
