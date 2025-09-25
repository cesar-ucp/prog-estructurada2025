#Ejercicio i modificado

#ENTRADA
suma = 0 
contador = 0

#PROCESO
for i in range(4):
    nota = float(input("ingrese la nota: "))
    suma = suma + nota #acumulador
    contador = contador + 1 #contador

#SALIDA
print("el promedio es: ", suma/contador)

# modificar el código para que el usuario ingrese las notas hasta que 
# ingrese el valor "fin", luego calcule el promedio