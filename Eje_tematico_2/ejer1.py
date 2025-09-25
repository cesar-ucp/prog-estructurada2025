def contarCadena(cadena,letra):
    cont = 0
    for caracter in cadena:
        if caracter == letra:
            cont += 1
    
    if cont == 0:
        return "No aparecio la letra"
    else:
        return f"La cantidad de veces que aparece la letra {letra} es {cont}"




print(contarCadena("Hola que tal como estas", "a"))
print(contarCadena("Clase de Programacion estructurada", "P"))
print(contarCadena("Clase de Programacion estructurada", "x"))