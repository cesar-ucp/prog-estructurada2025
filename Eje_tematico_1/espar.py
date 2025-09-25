def es_par(n: int) -> bool:
    """
    Función que evualua el argumento 'n' si devuelve True es PAR
    Si devuelve False es IMPAR

    """
    if n % 2 == 0:
        return True
    else:
        return False

def es_nota_valida(n:float) -> bool:
    """
    Funcion que evalua argumento n y devuelve TRUE si
    n es >= 1 y <= 10
    y devuelve FALSE en otro caso

    """
    if n >= 1 and n <= 10:
        return True
    else:
        return False
    
a = a + 1   
a =+ 1  # syntactic sugar o azucar sintactico

valor = es_par(4)
print(valor)
valor = es_par(5)
print(valor)

