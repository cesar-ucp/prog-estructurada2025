#Ejercicio

"""
Se tienen las ventas realizadas por los vendedores
Ana, Pedro y Juan durante los dias Lunes, Martes y Miercoles.
Generar una matriz donde se guarden las ventas
"""
import random

dias = ("lun", "mar", "mie") #tupla

vendedores = ["Ana", "Pedro", "Juan"] #lista

ventas = [] #lista

# forma de crear matriz de las ventas
ventas.append([20, 40, 10])
ventas.append([30, 20, 20])
ventas.append([10, 20, 15])

ventas[0][1] #devuelve el valor 40
ventas[2][2] #devuelve el valor 15

#Total de ventas de Ana
ventas_Ana = 0
for i in range(len(ventas)):
    ventas_Ana += ventas[0][i]

print(f"El total de ventas del vendedor {vendedores[0]} es {ventas_Ana}")

#Total de ventas de Pedro
ventas_Pedro = 0
for i in range(len(ventas)):
    ventas_Pedro += ventas[1][i]

print(f"El total de ventas del vendedor {vendedores[1]} es {ventas_Pedro}")

# y de Juan???

# Crear una lista que contenga el Total de ventas por vendedor
total_ventas_vendedor = []
acum = 0
for f in range(len(ventas)):
    for c in range(len(ventas)):
        acum += ventas[f][c]
    total_ventas_vendedor.append(acum)
    acum = 0

print("total ventas por vendedor: ", total_ventas_vendedor)

#Crear total de ventas por dia


