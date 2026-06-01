print("funciones en python para Language App")
print("funcion basica")


def saludar():
    print("Hola desde Language App")


saludar()

print("funcion con parametro")


def saludar_con_nombre(nombre):
    print(f"Hola: {nombre}, listo para practicar?")


saludar_con_nombre("John")
saludar_con_nombre("Maria")

print("funcion que devuelve valor con return")


def sumar_puntos(a, b):
    return a + b


print(sumar_puntos(4, 5))

print("funcion por posicion y por nombre")


def presentar_estudiante(nombre, edad, idioma):
    print(f"Estudiante: {nombre}, edad: {edad}, idioma: {idioma}")


presentar_estudiante("Maria", 26, "ingles")
presentar_estudiante("Carla", 29, "frances")
presentar_estudiante(edad=30, nombre="Luis", idioma="portugues")

print("funcion con valores de parametros por defecto")


def saludo_con_valores(nombre, saludo="Hola", puntuacion="!"):
    print(saludo, nombre, puntuacion)


saludo_con_valores("Pedro", "Buenas noches", "...")
saludo_con_valores("Juan", puntuacion="...")
saludo_con_valores("Luis", saludo="Buenas tardes")

print("funcion con parametros posicionales")


def sumar_todos(*args):
    print(f"Puntos recibidos {args}")
    return sum(args)


print(sumar_todos(1, 2, 3))
print(sumar_todos(1, 2, 3, 4, 5, 6, 7))
print(sumar_todos(10, 20, 30))

print("funcion parametros combinados posicionales")


def mostrar_info(titulo, *datos):
    print(f"Parametros recibidos {datos}, {titulo}")
    print(titulo)
    for dato in datos:
        print(f"-{dato}")


mostrar_info("Idiomas", "ingles", "frances", "portugues")

print("funcion parametros clave valor variables")


def crear_perfil(**kwargs):
    print(f"Parametros recibidos {kwargs}")
    for clave, valor in kwargs.items():
        print(f"{clave}-{valor}")


crear_perfil(nombre="Jimena", apellido="Paris", edad=20, idioma="ingles")

print("funcion parametros combinacion con todos los tipos")


def configurar(api_url, *idiomas, debug=False, **opciones):
    print("Configuracion")
    print(f"API URL: {api_url}")
    print(f"Idiomas: {idiomas}")
    print(f"Debug: {debug}")
    print(f"Opciones: {opciones}")


configurar("localhost", "ingles", "frances", "portugues", debug=True, timeout=30, ssl=True)

print("Devolver diccionario en el caso de muchos valores")


def analizar(puntajes):
    total = sum(puntajes)
    n = len(puntajes)
    return {
        "total": total,
        "media": total / n if n > 0 else 0,
        "minimo": min(puntajes) if puntajes else None,
        "maximo": max(puntajes) if puntajes else None,
        "count": n,
    }


datos = [12, 334, 2, 3, 4453, 3, 2, 3]
stats = analizar(datos)
print(f"Total: {stats['total']}")
print(f"Media: {stats['media']}")
print(f"Rango: {stats['minimo']}-{stats['maximo']}")
print(f"Cantidad: {stats['count']}")

print("Funciones lambda")


def doble(numero):
    return numero * 2


duplicar = lambda x: x * 2
print(doble(2))
print(duplicar(3))
suma = lambda a, b: a + b
print(suma(4, 5))
