a = "cotizacion.csv"

#Leer el archivo cotizacion y obtener el total de Volumen
with open(a, "r", encoding="utf-8") as file: 
    sumaVolumen = 0
    linea = file.readline()
    while linea != "":
        linea = file.readline()
        print(linea)
        
        #convertir la linea (str) en lista
        L = linea.split(";")
        print("La linea es " , L)
        #convierto en flotante el valor de volumen
        
        vol = vol.replace(".", "") # elimina los separadores de miles


        vol = L[4].replace(",", ".")# convierto coma decimal "," en punto decimal para Python "."
        
        volumen = float(vol) #volumen

        #acumula en una variable el volumen
        sumaVolumen += volumen

print(f"El total del volumen es: {sumaVolumen}")    
   

    