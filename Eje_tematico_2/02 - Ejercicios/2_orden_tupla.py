def esta_ordenada_recorrido(tupla_datos):
    """
    Verifica si una tupla está ordenada de menor a mayor iterando sobre los elementos.
    """
    # Una tupla con 0 o 1 elemento siempre se considera ordenada.
    if len(tupla_datos) <= 1:
        return True

    # Recorremos la tupla desde el segundo elemento (índice 1).
    # Comparamos cada elemento (tupla_datos[i]) con el anterior (tupla_datos[i-1]).
    for i in range(1, len(tupla_datos)):
        if tupla_datos[i-1] > tupla_datos[i]:
            # Si encontramos un elemento mayor que el siguiente, no está ordenada.
            return False
            
    # Si el bucle termina sin encontrar desorden, está ordenada.
    return True

# ----------------------------------------------------------------------
## Ejemplos de Uso de la Alternativa
# ----------------------------------------------------------------------

tupla_a = (1, 5, 8, 12)
tupla_b = (1, 8, 5, 12)

print(f"Recorrido: Tupla {tupla_a} ¿ordenada? {esta_ordenada_recorrido(tupla_a)}")
print(f"Recorrido: Tupla {tupla_b} ¿ordenada? {esta_ordenada_recorrido(tupla_b)}")