#Ejercicio 7.7.2
# punto a
def encajar_ficha(ficha1, ficha2):

    if( ficha1[0] == ficha2[0] or 
        ficha1[0] == ficha2[1] or
        ficha1[1] == ficha2[0] or
        ficha1[1] == ficha2[1]):
        return "Las fichas encajan"
    else:
        return "Las fichas no encajan"

a = (3,4)
b = (4,5)

print(encajar_ficha(a, b))
print(encajar_ficha((2,4), (5,10)))
print(encajar_ficha([5,9], [0,9]))


# ----------------------------------------------------
#punto b
def encajar_ficha(ficha1, ficha2):

    if( ficha1[0] == ficha2[0] or 
        ficha1[0] == ficha2[1] or
        ficha1[1] == ficha2[0] or
        ficha1[1] == ficha2[1]):
        return "Las fichas encajan"
    else:
        return "Las fichas no encajan"

ficha1 = "3-4"
ficha2 = "4-5"
a = ficha1.split("-")
b = ficha2.split("-")

print(encajar_ficha(a, b))
print(encajar_ficha((2,4), (5,10)))
print(encajar_ficha([5,9], [0,9]))
