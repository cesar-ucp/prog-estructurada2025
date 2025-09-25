from faker import Faker

dato = Faker("es_AR")

listaAlumnos = []

for i in range(10):
    nombre = dato.free_email()

    listaAlumnos.append(nombre)

print(listaAlumnos)

