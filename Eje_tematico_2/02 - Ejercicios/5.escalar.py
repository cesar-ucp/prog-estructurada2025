def producto_escalar_puro(vector1, vector2):
    """
    Calcula el producto escalar de dos vectores en Python puro.

    Args:
        vector1 (list): El primer vector.
        vector2 (list): El segundo vector.

    Returns:
        float: El producto escalar de los dos vectores.

    Raises:
        ValueError: Si los vectores no tienen la misma longitud.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud para calcular el producto escalar.")

    # La comprensión de lista multiplica los elementos correspondientes
    # (v1[i] * v2[i]) y sum() los agrega todos.
    return sum(v1_i * v2_i for v1_i, v2_i in zip(vector1, vector2))

# --- Ejemplo de uso ---
v_c = [10, 2, 5]
v_d = [3, 4, 1]

resultado_puro = producto_escalar_puro(v_c, v_d)
print(f"El producto escalar de {v_c} y {v_d} es: {resultado_puro}")
# Salida: El producto escalar de [10, 2, 5] y [3, 4, 1] es: 43
# (10*3) + (2*4) + (5*1) = 30 + 8 + 5 = 43