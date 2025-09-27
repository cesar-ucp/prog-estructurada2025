def encajan_domino(ficha1_str, ficha2_str):
    """
    Indica si dos fichas de dominó encajan.

    Las fichas encajan si tienen al menos un número en común.

    Args:
        ficha1_str (str): Cadena que representa la primera ficha (ej: "3-4").
        ficha2_str (str): Cadena que representa la segunda ficha (ej: "2-5").

    Returns:
        bool: True si las fichas encajan, False en caso contrario.
    """
    # 1. Usar split() para obtener los números de la primera ficha
    # Convertimos los strings resultantes a enteros para compararlos
    try:
        lados_ficha1 = [int(numero) for numero in ficha1_str.split('-')]
        lados_ficha2 = [int(numero) for numero in ficha2_str.split('-')]
    except ValueError:
        print("Error: Las fichas deben contener solo números separados por guion (-).")
        return False

    # 2. Asignar los valores a variables claras
    a, b = lados_ficha1
    c, d = lados_ficha2

    # 3. Comprobar si encajan
    # Las fichas encajan si algún extremo de la primera (a o b) es igual 
    # a algún extremo de la segunda (c o d).
    if a == c or a == d or b == c or b == d:
        return True
    else:
        return False

# ----------------------------------------------------------------------
## Ejemplos de Uso
# ----------------------------------------------------------------------

# Encajan (3-4 y 4-0) -> tienen el 4 en común
ficha_a = "3-4"
ficha_b = "4-0"
resultado_encajan = encajan_domino(ficha_a, ficha_b)
print(f"¿Las fichas {ficha_a} y {ficha_b} encajan? {resultado_encajan} ✅") 
# Salida: ¿Las fichas 3-4 y 4-0 encajan? True ✅

# No encajan (3-4 y 5-6)
ficha_c = "3-4"
ficha_d = "5-6"
resultado_no_encajan = encajan_domino(ficha_c, ficha_d)
print(f"¿Las fichas {ficha_c} y {ficha_d} encajan? {resultado_no_encajan} ❌")
# Salida: ¿Las fichas 3-4 y 5-6 encajan? False ❌

# Encajan (1-2 y 2-1) -> tienen el 2 y el 1 en común
ficha_e = "1-2"
ficha_f = "2-1"
resultado_doble_encaje = encajan_domino(ficha_e, ficha_f)
print(f"¿Las fichas {ficha_e} y {ficha_f} encajan? {resultado_doble_encaje} ✅")
# Salida: ¿Las fichas 1-2 y 2-1 encajan? True ✅

# Encajan (0-0 y 0-6) -> tienen el 0 en común
ficha_g = "0-0"
ficha_h = "0-6"
resultado_cero = encajan_domino(ficha_g, ficha_h)
print(f"¿Las fichas {ficha_g} y {ficha_h} encajan? {resultado_cero} ✅")
# Salida: ¿Las fichas 0-0 y 0-6 encajan? True ✅