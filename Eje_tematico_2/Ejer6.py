#ejercicio 6
from faker import Faker 

f = Faker("es_AR")

def crearAlumnos():
    listaAlumnos = []
    for i in range(10):
        listaAlumnos.append(f.name())
    return listaAlumnos

print(crearAlumnos())