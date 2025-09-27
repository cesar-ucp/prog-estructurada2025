def sumar_matrices(matriz1, matriz2):
    """
    Suma dos matrices (listas de listas).

    Args:
        matriz1 (list of list): La primera matriz.
        matriz2 (list of list): La segunda matriz.

    Returns:
        list of list or None: La matriz resultado de la suma, o None si las dimensiones no coinciden.
    """
    # 1. Verificar las dimensiones de las matrices

    # Obtener el número de filas (longitud de la lista principal)
    filas1 = len(matriz1)
    filas2 = len(matriz2)

    # Si tienen diferente número de filas, no se pueden sumar.
    if filas1 != filas2:
        print("Error: Las matrices deben tener el mismo número de filas.")
        return None

    # Si están vacías (0 filas), la suma es una matriz vacía.
    if filas1 == 0:
        return []

    # Obtener el número de columnas (longitud de la primera fila)
    columnas1 = len(matriz1[0])
    columnas2 = len(matriz2[0])

    # Verificar que todas las filas de la matriz 1 tengan la misma longitud
    for fila in matriz1:
        if len(fila) != columnas1:
            print("Error: La primera matriz no tiene todas las filas de igual longitud.")
            return None
    
    # Verificar que la matriz 2 tenga el mismo número de columnas que la matriz 1
    if columnas1 != columnas2:
        print("Error: Las matrices deben tener el mismo número de columnas.")
        return None
    
    # Verificar que todas las filas de la matriz 2 tengan la misma longitud
    for fila in matriz2:
        if len(fila) != columnas2:
            print("Error: La segunda matriz no tiene todas las filas de igual longitud.")
            return None

    # 2. Realizar la suma elemento por elemento
    
    # Inicializar la matriz resultado
    matriz_suma = []

    # Recorrer las filas
    for i in range(filas1):
        # Inicializar la fila actual de la matriz resultado
        nueva_fila = []
        
        # Recorrer las columnas
        for j in range(columnas1):
            # Sumar los elementos correspondientes
            suma_elemento = matriz1[i][j] + matriz2[i][j]
            nueva_fila.append(suma_elemento)
        
        # Añadir la fila sumada a la matriz resultado
        matriz_suma.append(nueva_fila)
        
    return matriz_suma

# ----------------------------------------------------------------------
## Ejemplos de Uso
# ----------------------------------------------------------------------

# Matrices que sí se pueden sumar (3x3)
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = sumar_matrices(A, B)
print("--- Matrices 3x3 que encajan ---")
print(f"Matriz A: {A}")
print(f"Matriz B: {B}")
print(f"Suma A + B: {C}")
# Resultado esperado: [[10, 10, 10], [10, 10, 10], [10, 10, 10]] ✅

# ---
# Matrices que no se pueden sumar (diferentes dimensiones)
D = [
    [1, 2],
    [3, 4]
]  # 2x2
E = [
    [5, 6, 7],
    [8, 9, 0]
]  # 2x3

F = sumar_matrices(D, E) # Esto imprimirá un mensaje de error
print("\n--- Matrices con dimensiones diferentes ---")
print(f"Matriz D: {D}")
print(f"Matriz E: {E}")
print(f"Suma D + E: {F}")
# Resultado esperado: None ❌

# ---
# Matrices con diferente número de filas
G = [
    [1, 2]
] # 1x2
H = [
    [3, 4],
    [5, 6]
] # 2x2

I = sumar_matrices(G, H) # Esto imprimirá un mensaje de error
print("\n--- Matrices con diferente número de filas ---")
print(f"Matriz G: {G}")
print(f"Matriz H: {H}")
print(f"Suma G + H: {I}")
# Resultado esperado: None ❌