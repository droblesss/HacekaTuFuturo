def interes_compuesto(cantidad,interes,ciclos):
    interes = interes / 100 + 1
    resultado = cantidad * interes**ciclos
    ganancia = resultado - cantidad
    return "La cantidad final será:" ,round(resultado), "y la ganancia total:" ,round(ganancia)


print(interes_compuesto(1000,8,10))