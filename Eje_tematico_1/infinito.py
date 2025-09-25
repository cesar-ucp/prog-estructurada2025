#Ejercicio 6
# ciclo definido (for)
# menorTiempo = float("inf")
# for i in range(3): 
# 	nroVehiculo = input("Nro de vehiculo:")
# 	tiempo = float(input("Ingrese el tiempo en segundos."))	

# 	if tiempo < menorTiempo:        
# 		menorTiempo = tiempo
# 		vehicMenorTiempo = nroVehiculo
    
# print(f"El menor vehiculo tuvo el tiempo {menorTiempo} con el numero de vehiculo {vehicMenorTiempo}")

#ciclo indefinido (while)
contador = 1
menorTiempo = float("inf")
while contador <= 3:
	nroVehiculo = input("Nro de vehiculo:")
	tiempo = float(input("Ingrese el tiempo en segundos."))	

	if tiempo < menorTiempo:        
		menorTiempo = tiempo
		vehicMenorTiempo = nroVehiculo
	contador += 1
    
print(f"El menor vehiculo tuvo el tiempo {menorTiempo} con el numero de vehiculo {vehicMenorTiempo}")
print(contador)
