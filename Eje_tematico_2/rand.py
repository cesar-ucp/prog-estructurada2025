import random
print(random.randint(10,20))

#1 forma hardcodeado
Ventas = [ [20, 30, 10], [30, 20, 20],[10, 20, 30] ] 

#2 forma pedirle al usuario
ventas = []
filas = 3
colum = 3

for f in range(filas):
    for c in range(colum):
        venta = float(input("Ingrese venta: "))
        ventas[f][c] = venta

#3 forma: generar valores random
for f in range(filas):
    for c in range(colum):
        venta = random.randint(20, 60)
        ventas[f][c] = venta

#4 forma 
venta_vendedor = []
venta_vendedor.append(20)
venta_vendedor.append(30)
venta_vendedor.append(10)
ventas[0].append(venta_vendedor)

venta_vendedor = []
venta_vendedor.append(30)
venta_vendedor.append(20)
venta_vendedor.append(20)
ventas[1].append(venta_vendedor)

venta_vendedor = []
venta_vendedor.append(10)
venta_vendedor.append(20)
venta_vendedor.append(30)
ventas[2].append(venta_vendedor)