print("Ciclo while en Language App")

contador = 1
while contador <= 5:
    print(f"Palabra nueva {contador}")
    contador += 1

dato = ""
while dato != "salir":
    dato = input("Escribe una palabra aprendida (salir para terminar): ")
    print(f"Registraste: {dato}")

cantidad = int(input("Cuantas lecciones compro? "))
total = 0
contador = 1
while contador <= cantidad:
    precio = float(input(f"Precio de la leccion {contador}: "))
    total += precio
    contador += 1

print("total", total)
if total >= 100:
    print("Aplica descuento de estudiante")
else:
    print("No aplica descuento")

estudiantes = int(input("Cuantos estudiantes registrara? "))
total_puntos = 0
contador = 1
while contador <= estudiantes:
    puntos = float(input(f"Puntos del estudiante {contador}: "))
    total_puntos += puntos
    contador += 1

print("total de puntos", total_puntos)
if total_puntos >= 1000:
    print("Grupo con avance alto")
else:
    print("Grupo con avance controlado")
