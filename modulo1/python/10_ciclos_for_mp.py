print("ciclo for en Language App")
print("for clasico")
for i in range(1, 6):
    print(f"Leccion {i}")

idiomas = ["ingles", "frances", "portugues"]
for idioma in idiomas:
    print(idioma)

print("control de interrupcion")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print(f"Ejercicio {i}")
else:
    print("Terminado el ciclo")

print("for con range step")
for i in range(1, 10, 2):
    print(f"Practica impar {i}")

print("for con range regresivo")
for i in range(10, 0, -1):
    print(f"Cuenta regresiva para reto: {i}")

print("for con range enumerante")
usuarios = ["juan", "luis", "pedro", "maria"]
for indice, usuario in enumerate(usuarios):
    print(indice, usuario)

print("for con range zip")
puntajes = [18, 11, 25, 56]
for usuario, puntaje in zip(usuarios, puntajes):
    print(usuario, puntaje)

print("for anidados")
for unidad in range(1, 4):
    for leccion in range(1, 4):
        print(unidad, leccion)

cantidad = int(input("Ingrese cantidad de notas de lecciones: "))
suma = 0
for i in range(1, cantidad + 1):
    nota = float(input(f"Nota {i}: "))
    suma += nota

promedio = suma / cantidad
print("Promedio:", promedio)
if promedio >= 7:
    print("Curso aprobado")
else:
    print("Debe repasar mas")
