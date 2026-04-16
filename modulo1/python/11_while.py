print("Ciclo while")
contador=1
while contador<=5:
    print(contador)
    contador+=1
    
dato=""
while dato!="salir":
    dato = input("Escribe algo (salir para terminar)")
    print(f"escribiste: {dato}")
    

cantidad=int(input("Cuantos productos compro"))
total=0
contador=1
while contador<=cantidad:
    precio = float(input(f"precio del producto {contador}: "))
    total+=precio
    contador+=1
print("total", total)
if total>=100:
    print("aplica descuneto")
else:
    print("no aplica descuenta")
    

#ejercicio

empleados=int(input("Cuantos empleador registrara"))
total=0
contador=1
while contador<=empleados:
    salario = float(input(f"salario del trabajador {contador}: "))
    total+=salario
    contador+=1
print("total", total)
if total>=1000:
    print("Gasto alto")
else:
    print("Gasto controlado")