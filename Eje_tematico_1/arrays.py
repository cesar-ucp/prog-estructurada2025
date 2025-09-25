
# Contar cuantas veces aparece la letra 'a'
texto = "Hola que tal como te va"

contador = 0
for letra in texto:
    if letra == "a":
        contador = contador + 1
print(f"La cantidad de veces que aparece 'a' es {contador}")