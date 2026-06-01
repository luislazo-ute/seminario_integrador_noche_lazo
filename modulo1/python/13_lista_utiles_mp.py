print("Manipulacion de listas en Language App")
print("Crear listas")

vacia = []
print(vacia)
puntajes = [1, 2, 3, 4, 5]
print(puntajes)
estudiantes = ["Juan", "Juana", "Jose", "Yamil"]
print(estudiantes)
mixta = [1, 3, "Hello", True, "Language", None, 3.14]
print(mixta)
anidada = [1, 2, ["hello", "hola"], 5, ["bye", ["adios", "ciao"]]]
print(anidada)

print("Acceso a los elementos de una lista")
print(estudiantes[1])
print(estudiantes[-1])
print(estudiantes[1:3])
print(estudiantes[::-1])

print("CRUD de una lista")
idiomas = ["ingles", "frances", "portugues", "italiano"]
print(idiomas)
idiomas.insert(1, "aleman")
print(idiomas)
idiomas.append(["japones"])
print(idiomas)
idiomas.append(["coreano", "mandarin"])
print(idiomas)
idiomas[0] = "ingles avanzado"
print(idiomas)
idiomas.remove("ingles avanzado")
print(idiomas)
eliminados = idiomas.pop()
print(eliminados)
print(idiomas)
eliminados = idiomas.pop(2)
print(eliminados)
print(idiomas)
del idiomas[0]
print(idiomas)

print("Buscar valores en los elementos de una lista")
print("aleman" in idiomas)
print(idiomas.index("frances"))
print(idiomas.count("frances"))

print("Ordenar una lista")
puntajes_desordenados = [3, 2, 9, 5, 4, 1]
print(puntajes_desordenados)
puntajes_desordenados.sort()
print(puntajes_desordenados)
puntajes_desordenados.sort(reverse=True)
print(puntajes_desordenados)
ordenada = sorted(puntajes_desordenados)
print(ordenada)
print(puntajes_desordenados)
