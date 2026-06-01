print("Condicional if en Language App")
print("if simple")
lecciones_disponibles = 3
if lecciones_disponibles > 0:
    print("Hay lecciones disponibles")

print("if else - dos caminos")
puntos = 25
if puntos > 0:
    print("Puede iniciar una practica")
else:
    print("Necesita ganar puntos")

print("if multiples condiciones")
progreso = 72
if progreso < 30:
    print("Nivel inicial")
elif progreso < 70:
    print("Nivel intermedio")
else:
    print("Nivel avanzado")

print("if condiciones anidadas")
conexion = True
token_valido = False
if conexion:
    if token_valido:
        print("Acceso a la API de lecciones")
    else:
        print("Token invalido para Language App")
else:
    print("Sin conexion")

print("if con operadores logicos")
perfil_completo = True
curso_seleccionado = True
if perfil_completo and curso_seleccionado:
    print("Inscripcion al curso confirmada")

es_premium = False
tiene_prueba_gratis = True
if es_premium or tiene_prueba_gratis:
    print("Puede usar ejercicios avanzados")

bloqueado = False
if not bloqueado:
    print("Usuario habilitado para practicar")

tipo_usuario = input("Ingrese su tipo de usuario (gratis/premium): ").lower()
ha_pagado = input("Ha pagado? (si/no): ").lower()

if tipo_usuario == "premium" and ha_pagado == "si":
    print("Acceso completo a idiomas")
elif tipo_usuario == "premium" and ha_pagado == "no":
    print("Debe pagar para desbloquear todos los idiomas")
else:
    print("Acceso limitado a lecciones basicas")
