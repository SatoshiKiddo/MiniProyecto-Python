from logic import Sandwich
from PyInquirer import prompt



welcomeMessage = "**************************\n" \
    "*    SANDWICHES UCAB     *\n" \
    "**************************"
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
                'name': 'Doble Queso'
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
                'value': 1
            },
            {
                'key': '2',
                'name': '20%',
                'value': 2
            },
            {
                'key': '3',
                'name': '30%',
                'value': 3
            },
            {
                'key': '4',
                'name': '40%',
                'value': 4
            },
            {
                'key': '5',
                'name': '50%',
                'value': 5
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
    print(f"******SANDWICH NUMERO {sandwichCounter}******")
    print("Opciones:")
    print("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ):")

    sandwichPropertys = prompt(sandwich)
    newSandwich.tipoSandwich(sandwichPropertys['size'])
    ingredients = sandwichPropertys['ingredientes']
    newSandwich.agregarIngredientes(ingredients)

    print()
    print(f"Usted eligio un sandiwch {newSandwich.tipo} con queso.")
    if ingredients:
        print(f"Aparte se ha añadido:", *ingredients, sep=",")
    print(f"el subtotal por este sandwich es: {newSandwich.getPrice()}")
    sandwichList.append(newSandwich)

    print("******************************")
    shouldKeepGoing = prompt(keepGoing)['keepGoing']
    if not shouldKeepGoing:
        break
    print("******************************")


while True:
    print()
    print("Opciones:")
    print("Porcentajes: Ninguro ( 0 ) 10% ( 1 ) 20% ( 2 ) 30% ( 3 ) 40% ( 4 ) 50% ( 5 ):")
    cuponPropertys = prompt(cupon)
    
    shouldKeepGoing = prompt(keepGoing)['keepGoing']
    if not shouldKeepGoing:
        break
    print("******************************")


total = 0
for sandwich in sandwichList:
    total += sandwich.getPrice()


if cuponPropertys['porcentaje'] == 1:
    total = total-(total*0.1)

if cuponPropertys['porcentaje'] == 2:
    total = total-(total*0.2) 

if cuponPropertys['porcentaje'] == 3:
    total = total-(total*0.3)

if cuponPropertys['porcentaje'] == 4:
    total = total-(total*0.4)

if cuponPropertys['porcentaje'] == 5:
    total = total-(total*0.5)


print(f"el pedido tiene un total de {sandwichCounter} sandwiches. Y un monto total de {total}")
