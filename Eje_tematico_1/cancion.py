
def es_numerico(c):
    for x in c:
        if not (x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x=="5" or x == "6" or x == "7" or x == "8" or x == "9"):
            return False
    return True
    

cad1 = "534a534"
cad2 = "534534"
cad3 = "aannbb"
# print(es_numerico(cad1)) #False
# print(es_numerico(cad2)) #True
# print(es_numerico(cad3)) #False

print(cad1.isdecimal())
print(cad2.isdecimal())
print(cad3.isdecimal())

elem = ["PERRO", "perro", "gato", "canario" ]
print(max(elem))
print(min(elem))
