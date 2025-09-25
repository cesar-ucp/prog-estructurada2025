NOMBRE_APP = "Sistema1" # variable global

def sumar_cuadrados(n):
    
    suma = 0
    for x in range(1, n + 1):
        suma = suma + calcular_cuadrado(x)
    return suma

def calcular_cuadrado(num):
    return num * num

y = sumar_cuadrados(5)

print("la suma es: ",y)