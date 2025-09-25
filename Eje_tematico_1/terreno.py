#Ejercicio del terreno

#ENTRADA
ancho_de_terreno = int(input("Ingrese ancho del terreno en metros: "))
largo_de_terreno = int(input("Ingrese largo del terreno en metros: "))
precio_m2 = int(input("Ingrese precio del terreno en metro cuadrado: "))
# cant_pasadas = int(input("Ingrese cant pasadas: "))

cant_pasadas = 3

#PROCESO
precio_terreno = ancho_de_terreno * largo_de_terreno * precio_m2
metros_alambre = ((2 * ancho_de_terreno) + (2 * largo_de_terreno)) * cant_pasadas #esto esta hardcodeado

#SALIDA
#print("El precio del terreno en m2 es", precio_terreno, "Metros de alambre para 3 pasadas es:",metros_alambre)
print(f"El precio del terreno en m2 es {precio_terreno} Metros de alambre para 3 pasadas es {metros_alambre}")