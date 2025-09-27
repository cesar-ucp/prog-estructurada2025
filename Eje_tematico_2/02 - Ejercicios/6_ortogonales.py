def son_ortogonales(vector1, vector2):
    """
    Comprueba si dos vectores son ortogonales.

    Args:
        vector1 (list o tuple): El primer vector.
        vector2 (list o tuple): El segundo vector.

    Returns:
        bool: True si los vectores son ortogonales, False en caso contrario.
        
    Raises:
        ValueError: Si los vectores tienen diferente longitud.
    """
    
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud para calcular el producto escalar.")
        
    # Calcular el producto escalar (dot product)
    # Se suman los productos de los componentes correspondientes
    producto_escalar = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    
    # Si el producto escalar es cero, los vectores son ortogonales.
    # Usamos una pequeña tolerancia (como 1e-9) para comparación con cero 
    # si los vectores contienen números de punto flotante (floats),
    # pero para simplicidad y si esperamos enteros, '== 0' es suficiente.
    # Usaremos una tolerancia para robustez.
    tolerancia = 1e-9
    
    return abs(producto_escalar) < tolerancia

# --- Ejemplos de uso ---

# Ejemplo 1: Vectores ortogonales (producto escalar = 3*(-6) + 1*(18) = -18 + 18 = 0)
v_ortogonal_1 = [3, 1]
v_ortogonal_2 = [-6, 18]
print(f"¿{v_ortogonal_1} y {v_ortogonal_2} son ortogonales? {son_ortogonales(v_ortogonal_1, v_ortogonal_2)}") 
# Salida: ¿[3, 1] y [-6, 18] son ortogonales? True

# Ejemplo 2: Vectores NO ortogonales (producto escalar = 1*2 + 2*3 = 2 + 6 = 8)
v_no_ortogonal_1 = [1, 2]
v_no_ortogonal_2 = [2, 3]
print(f"¿{v_no_ortogonal_1} y {v_no_ortogonal_2} son ortogonales? {son_ortogonales(v_no_ortogonal_1, v_no_ortogonal_2)}") 
# Salida: ¿[1, 2] y [2, 3] son ortogonales? False

# Ejemplo 3: Vectores en 3D (producto escalar = 1*(-2) + 2*1 + 3*0 = -2 + 2 + 0 = 0)
v_3d_1 = [1, 2, 3]
v_3d_2 = [-2, 1, 0]
print(f"¿{v_3d_1} y {v_3d_2} son ortogonales? {son_ortogonales(v_3d_1, v_3d_2)}")
# Salida: ¿[1, 2, 3] y [-2, 1, 0] son ortogonales? True

# Ejemplo 4: Vectores con floats
v_float_1 = [0.5, 1.0]
v_float_2 = [2.0, -1.0]
print(f"¿{v_float_1} y {v_float_2} son ortogonales? {son_ortogonales(v_float_1, v_float_2)}")
# Salida: ¿[0.5, 1.0] y [2.0, -1.0] son ortogonales? False (0.5*2.0 + 1.0*(-1.0) = 1.0 - 1.0 = 0, ¡es True!)
# Salida corregida: ¿[0.5, 1.0] y [2.0, -1.0] son ortogonales? True (La función con tolerancia maneja esto correctamente)