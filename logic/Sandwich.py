#coding=utf-8
from .Ingrediente import Ingrediente
import itertools

class Sandwich:

    precio_base = 280
    precio_doble = 430
    precio_triple = 580
    ingredientes_adicionales_base = [
        Ingrediente(40, "Jamon"),
        Ingrediente(35, "Champiñones"),
        Ingrediente(30, "Pimentón"),
        Ingrediente(40, "Doble queso"),
        Ingrediente(57.5, "Aceitunas"),
        Ingrediente(38.5, "Pepperoni"),
        Ingrediente(62.5, "Salchichón")
    ]

    def individual(self):
        self.tipo = "Individual"
        self.precio = self.precio_base
    
    def doble(self):
        self.tipo = "Doble"
        self.precio = self.precio_doble

    def triple(self):
        self.tipo = "Triple"
        self.precio = self.precio_triple

    def tipoSandwich(self, tipo):
        if ( tipo == 1):
            self.individual()
        elif( tipo == 2):
            self.doble()
        else:
            self.triple()

    def __init__(self, tipo):
        self.ingredientes_adicionales = []
        self.tipoSandwich(tipo)

    def agregarIngrediente(self, ingrediente_adicional):
        self.ingredientes_adicionales.append(self.ingredientes_adicionales_base[ingrediente_adicional])
        self.precio = self.ingredientes_adicionales[ingrediente_adicional].getPrecio()

    def agregarIngredientes(self, ingredientes):
        for ingrediente in ingredientes:
            nuevoIngrediente = self.__searchIngredient(ingrediente)
            self.ingredientes_adicionales.append( nuevoIngrediente )


    def getIngredientesAdicionales(self):
        print("Ingredientes adicionales: \n")
        for ingrediente in self.ingredientes_adicionales:
            print(ingrediente.getNombre() + ' - ' + str(ingrediente.getPrecio()) )

    def getTipoSandwich(self):
        print('Tipo de sandwich: ' + self.tipo + '\n')


    def __searchIngredient(self, ingredientName):
        for ingredient in self.ingredientes_adicionales_base:
            if (ingredient.getNombre() == ingredientName ):
                return ingredient


    def getPrice(self):
        totalIngredients = 0
        for ingredient in self.ingredientes_adicionales:
            totalIngredients += ingredient.getPrecio()

        return self.precio + totalIngredients        
        