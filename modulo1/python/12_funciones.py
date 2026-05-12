print("funciones en python")
print("función basica")
def saludar():
    print("Hola desde la UTE")
    
saludar()


print("funcion con parametro")
def saludarConNombre(nombre):
    print(f"Hola: {nombre}, Que tal?")
    
saludarConNombre("John")
saludarConNombre("Maria")

print("funcion que devuelve valor con return")
def sumar(a, b):
    return a+b
print(sumar(4,5))

print("funcion por posicion y por nombre")
def presentar(nombre, edad, ciudad):
    print(f"Señor(a): {nombre}, edad: {edad}, ciudad: {ciudad}")


presentar("Maria", 26, "Quito")
presentar("Carla", 29, "Guayaquil")
presentar(edad=30,nombre="Luis",ciudad="Quito")


print("funcion con valores de parametros por defecto")
def saludo_con_valores(nombre, saludo="Hola", puntuacion="!"):
    print(saludo, nombre, puntuacion)
    
saludo_con_valores("Pedro", "Buenas noches", "...")
saludo_con_valores("Juan", puntuacion= "...")
saludo_con_valores("Luis", saludo="Buenas tardes")


print("funcion con parametros posicionales")
def sumar_todos(*args):
    print(f"Parametros recibidos {args}")
    return sum(args)
print(sumar_todos(1,2,3))
print(sumar_todos(1,2,3,4,5,6,7))
print(sumar_todos(10,20,30))


print("funcion parametros combinados posicionales")
def mostrar_info(titulo,*datos):
    print(f"Parametros recibidos {datos}, {titulo}")
    
    print(titulo)
    for dato in datos:
        print(f"-{datos}")
mostrar_info("Frutas","naranja","pera","manzana")

print("funcion parametros clave valor variables")
def crear_perfil(**kwargs):
    print(f"Parametros recibidos {kwargs}")
    for clave, valor in kwargs.items():
        print(f"{clave}-{valor}")
crear_perfil(nombre="Jimena", apellido="paris", edad=20, ciudad="punto fijo")

print("funcion parametros combinacion con todos los tipos")
def configurar(host, *puertos, debug=False, **opciones):
    print(f"Configuracion")
    print(f"Host: {host}")
    print(f"Puertos: {puertos}")
    print(f"Debug: {debug}")
    print(f"Opciones: {opciones}")
configurar("localhost", 80, 443, 8080, debug=True, timeout=30, ssl=True)

print("Devolver diccionario en el caso de muchos valores")
def analizar(numeros):
    total=sum(numeros)
    n=len(numeros)
    return {
        "total": total,
        "media": total/n if n>0 else 0,
        "minimo": min(numeros) if numeros else None,
        "maximo": max(numeros) if numeros else None,
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
duplicar=lambda x : x*2
print(doble(2))
print(duplicar(3))
suma=lambda a,b: a+b
print(suma(4,5))