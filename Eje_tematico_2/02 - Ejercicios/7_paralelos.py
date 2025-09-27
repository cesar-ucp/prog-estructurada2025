def son_paralelos(vector1, vector2, tolerancia=1e-9):
    """
    Verifica si dos vectores son paralelos.

    Dos vectores son paralelos si uno es un múltiplo escalar del otro.
    Maneja el caso especial de un vector cero.

    Args:
        vector1 (list o tuple): El primer vector.
        vector2 (list o tuple): El segundo vector.
        tolerancia (float): Umbral para la comparación de punto flotante.

    Returns:
        bool: True si los vectores son paralelos, False en caso contrario.
    """

    # 1. Verificar que tengan la misma dimensión
    if len(vector1) != len(vector2):
        return False  # Vectores de diferente dimensión no pueden ser paralelos

    dimension = len(vector1)

    # 2. Manejar el caso de vectores cero
    es_cero1 = all(abs(c) < tolerancia for c in vector1)
    es_cero2 = all(abs(c) < tolerancia for c in vector2)

    # Si al menos uno es el vector cero, son paralelos (por definición)
    if es_cero1 or es_cero2:
        return True

    # 3. Encontrar el factor escalar (k)
    # Buscamos el primer componente no cero para calcular el factor escalar 'k'.
    # Si vector2 = k * vector1, entonces k = vector2[i] / vector1[i]
    k = None
    
    for i in range(dimension):
        # Encontrar un componente no cero en vector1
        if abs(vector1[i]) >= tolerancia:
            # Calcular el factor escalar basado en este componente
            k = vector2[i] / vector1[i]
            break

    # Si k sigue siendo None, significa que vector1 es el vector cero (ya manejado)
    # o solo tiene ceros, pero el primer chequeo debería haberlo capturado.
    if k is None:
        return False # Esto no debería ocurrir si el chequeo de vector cero es correcto

    # 4. Verificar la proporcionalidad para el resto de los componentes
    # Comprobar que vector2[i] es aproximadamente igual a k * vector1[i]
    for i in range(dimension):
        # La comparación de punto flotante debe usar una tolerancia
        if abs(vector2[i] - k * vector1[i]) >= tolerancia:
            return False  # No son proporcionales, por lo tanto no son paralelos

    return True



## Ejemplos de Uso


# Vectores paralelos (mismo sentido)
v_a = [1, 2, 3]
v_b = [2, 4, 6]
print(f"v_a: {v_a}, v_b: {v_b} -> Paralelos: {son_paralelos(v_a, v_b)}")
# Salida: v_a: [1, 2, 3], v_b: [2, 4, 6] -> Paralelos: True (k=2)

# Vectores paralelos (sentido opuesto)
v_c = [4, -8]
v_d = [-1, 2]
print(f"v_c: {v_c}, v_d: {v_d} -> Paralelos: {son_paralelos(v_c, v_d)}")
# Salida: v_c: [4, -8], v_d: [-1, 2] -> Paralelos: True (k=-1/4 o -4)

# Vectores NO paralelos
v_e = [1, 0]
v_f = [0, 1]
print(f"v_e: {v_e}, v_f: {v_f} -> Paralelos: {son_paralelos(v_e, v_f)}")
# Salida: v_e: [1, 0], v_f: [0, 1] -> Paralelos: False

# Vector cero
v_g = [0, 0, 0]
v_h = [5, 10, 15]
print(f"v_g: {v_g}, v_h: {v_h} -> Paralelos: {son_paralelos(v_g, v_h)}")
# Salida: v_g: [0, 0, 0], v_h: [5, 10, 15] -> Paralelos: True