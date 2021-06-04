from logic import Sandwich
from PyInquirer import prompt
from os import system



welcomeMessage = "-------------------------------------------------------\n" \
    "|                  SANDWICHES UCAB                    |\n" \
    "-------------------------------------------------------"
print(welcomeMessage)


# sandwich questions
sandwich = [
    {
        'type': 'expand',
        'name': 'size',
        'message': 'de que tamaño quiere su sandwich',
        'choices': [
            {
                'key': 't',
                'name': 'Triple',
                'value': 3
            },
            {
                'key': 'd',
                'name': 'Doble',
                'value': 2
            },
            {
                'key': 'i',
                'name': 'Individual',
                'value': 1
            }
        ]
    },
    {
        'type': 'checkbox',
        'message': 'Seleccione ingredientes adicionales',
        'name': 'ingredientes',
        'choices': [
            {
                'name': 'Jamon'
            },
            {
                'name': 'Champiñones'
            },
            {
                'name': 'Pimentón'
            },
            {
                'name': 'Doble queso'
            },
            {
                'name': 'Aceitunas'
            },
            {
                'name': 'Pepperoni'
            },
            {
                'name': 'Salchichón'
            }
        ]
    }
]

#opciones de cupon
cupon = [
    {
        'type': 'expand',
        'name': 'porcentaje',
        'message': 'Seleccione el porcentaje del cupon',
        'choices': [
            {
                'key': '0',
                'name': 'Ninguno',
                'value': 0
            },
            {
                'key': '1',
                'name': '10%',
                'value': 10
            },
            {
                'key': '2',
                'name': '20%',
                'value': 20
            },
            {
                'key': '3',
                'name': '30%',
                'value': 30
            },
            {
                'key': '4',
                'name': '40%',
                'value': 40
            },
            {
                'key': '5',
                'name': '50%',
                'value': 50
            }

        ]
    }
]

delivery =[
{
        'type': 'expand',
        'name': 'delivery',
        'message': '¿La orden es para un delivery? [y/n]',
        'choices': [
            {
                'key': 'y',
                'name': 'Si',
                'value': 'Si'
            },
            {
                'key': 'n',
                'name': 'No',
                'value': 'No'
            }

        ]
    }
]

keepGoing = [
    {
        'type': 'confirm',
        'name': 'keepGoing',
        'message': 'Desea Continuar',
        'default': True,
    },
]


sandwichList = []
sandwichCounter = 0


while True:
    newSandwich = Sandwich(1)
    sandwichCounter += 1
    print()
    print("-------------------------------------------------------")
    print(f"|                  SANDWICH NUMERO {sandwichCounter}                  |")
    print("-------------------------------------------------------")
    print("Opciones:")
    print("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ):")

    sandwichPropertys = prompt(sandwich)
    newSandwich.tipoSandwich(sandwichPropertys['size'])
    ingredients = sandwichPropertys['ingredientes']
    newSandwich.agregarIngredientes(ingredients)

    print()
    system("cls")
    print(f"Usted eligio un sandiwch {newSandwich.tipo} con queso.")
    if ingredients:
        print(f"Aparte se ha añadido:", *ingredients, sep=",")
    print(f"el subtotal por este sandwich es: {newSandwich.getPrice()}")
    sandwichList.append(newSandwich)

    print("-------------------------------------------------------")
    shouldKeepGoing = prompt(keepGoing)['keepGoing']
    if not shouldKeepGoing:
        break
    print("-------------------------------------------------------")


while True:
    print()
    system("cls")
    print("Cupon:")
    print("Porcentajes: Ninguro ( 0 ) 10% ( 1 ) 20% ( 2 ) 30% ( 3 ) 40% ( 4 ) 50% ( 5 ):")
    cuponPropertys = prompt(cupon)

    print()
    system("cls")
    print("Delivery:")
    deliveryPropertys = prompt(delivery)
    
    shouldKeepGoing = prompt(keepGoing)['keepGoing']
    if not shouldKeepGoing:
        break
    print("-------------------------------------------------------")


total = 0
empaque = 0

for sandwich in sandwichList:
    total += sandwich.getPrice()

totalSinAdicionales = total


if cuponPropertys['porcentaje'] == 10:
    total = total-(total*0.1)

if cuponPropertys['porcentaje'] == 20:
    total = total-(total*0.2) 

if cuponPropertys['porcentaje'] == 30:
    total = total-(total*0.3)

if cuponPropertys['porcentaje'] == 40:
    total = total-(total*0.4)

if cuponPropertys['porcentaje'] == 50:
    total = total-(total*0.5)

if deliveryPropertys['delivery'] == 'Si':
    empaque = 10*sandwichCounter
    total += empaque    

system("cls")
print("-------------------------------------------------------")
print("|                  SANDWICHES UCAB                    |")
print("-------------------------------------------------------")
print(f"No. de sandwiches {sandwichCounter}")
print(f"Descuento {cuponPropertys['porcentaje']}%")
print(f"Cobro adicional por empaque para delivery.......${empaque}")
print(f"Monto sin descuentos ni adicionales ............${totalSinAdicionales}")
print(f"Monto total ....................................${total}")
