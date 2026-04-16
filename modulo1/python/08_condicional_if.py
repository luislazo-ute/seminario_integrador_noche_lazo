print("Condicional if")
print("if simple")
stock=3
if stock>0:
    print("Producto disponible")

print("if else - dos caminos")
saldo=25
if saldo>0:
    print("Compra permitida")
else:
    print("Saldo insuficiente")
    
print("if multiples condiciones")
temperatura=32
if temperatura<10:
    print("Hace frio")
elif temperatura<25:
    print("Clima templado")
else:
    print("Hace calor")
    
print("if condiciones anidadas")
conexion=True
token_valido=False
if conexion:
    if token_valido:
        print("Acceso a la api")
    else:
        print("Token invalido")
else:
    print("Sin conexion")

print("if con operadores logicos") 
documento=True
pago=True
if documento and pago:
    print("Inscripcion confirmada")

es_vip=False
tiene_invitacion=True
if es_vip or tiene_invitacion:
    print("Puede entrar al evento")
    
bloqueado=False

if not bloqueado:
    print("usuario habilitado") 
    


#Ejercio

tipo_usuario = input("Ingrese su tipo de usuario (gratis/premium): ").lower()
ha_pagado = input("¿Ha pagado? (si/no): ").lower()

if tipo_usuario == "premium" and ha_pagado == "si":
    print("Acceso completo")
elif tipo_usuario == "premium" and ha_pagado == "no":
    print("Debe pagar")
else:
    print("Acceso limitado")


