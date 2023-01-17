#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.

#Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.

#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


def pizza(x=input("¿Eres vegetarianx?")):
    if (x.upper() == "SI"):
        opcion = "vegetariana"
        ingrediente = input("Puedes elegir entre pimiento o tofu para tu pizza.Pulsa 1 para piminento o 2 para tofu")
        if (ingrediente == "1"):
            ingrediente = "pimiento"
        elif (ingrediente == "2"):
            ingrediente = "tofu"
        return ("Tu pizza será" ,opcion, "y los ingredientes:" ,ingrediente, "tomate y mozarella" )
    elif (x.upper() == "NO"):
        opcion = "no vegetariana"
        ingrediente = input("Puedes elegir entre peperoni,jamon y salmón para tu pizza.Pulsa 1 para peperoni, 2 para jamon o 3 para salmón")
        if (ingrediente == "1"):
            ingrediente = "peperoni"
        elif (ingrediente == "2"):
            ingrediente = "jamon"
        elif (ingrediente == "3"):
            ingrediente = "salmon"
        return ("Tu pizza será" ,opcion, "y los ingredientes:" ,ingrediente, "tomate y mozarella" )
    else:
        return ("Respuesta Inválida, prueba otra vez")
print(pizza("Si"))