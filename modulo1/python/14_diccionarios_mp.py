print("Diccionarios en Language App")
print("Crear Diccionarios")

vacio = {}
estudiante = {"nombre": "Pedro", "edad": 26, "idioma": "ingles"}
config = dict(api_url="localhost", puerto=8000)

print(vacio)
print(config)

print(estudiante["nombre"])
estudiante["nombre"] = "Jose"
print(estudiante)
del estudiante["edad"]
print(estudiante)

print("nombre" in estudiante)
print("idioma" in estudiante)

print(estudiante.keys())
print(estudiante.values())
print(estudiante.items())

for clave, valor in estudiante.items():
    print(f"clave: {clave}, valor: {valor}")
