cadena_string="Hola", "Desde", "La", "Ute"
print(cadena_string)
print("Hola", "Desde", "La", "Ute")
print("Hola", "Desde", "La", "Ute", sep=",")
print("Hola", "Desde", "La", "Ute", sep="-")
print("Hola", "Desde", "La", "Ute", end="")
print("Hola", "Desde", "La", "Ute", sep="-")
print("Hola", "Desde", "La", "Ute", end="|")
print("Hola", "Desde", "La", "Ute", end="|")

nombre="Maria Ramos"
edad=29
print("\n",nombre, edad)
nombre_edad = f"Nombre:{nombre}, {edad}"
print(nombre_edad)
print(f"Nombre: {nombre}, {edad}")
print(f"Doble de {edad} es {edad*2}")
print(f"{'Maria':>15}") #alineado a la derecha
pi=3.14159
print(f"{pi:.2f}")
print(f"{100000000000000000000000:,}")