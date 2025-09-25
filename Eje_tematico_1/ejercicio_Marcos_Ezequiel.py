#ENTRADA
#Marcos Ezequiel
suma = 0
contador = 0
_ = 3
#PROCESO
while True:
    nota = input("Ingrese la nota o escriba Fin para terminar= ")
    if nota == "fin":
        break
    suma = suma + float(nota) #acumulador
    contador = contador + 1 #contador

#SALIDA
if contador > 0:
    print("El promedio es: ", suma/contador)
else:
    print("No se ingresaron notas.")