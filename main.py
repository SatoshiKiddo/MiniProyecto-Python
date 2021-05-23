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


total = 0
for sandwich in sandwichList:
    total += sandwich.getPrice()


print(f"el pedido tiene un total de {sandwichCounter} sandwiches. Y un monto total de {total}")
