print("Match - case en Language App")
comando = input("Comando practicar/repasar/salir: ")

match comando:
    case "practicar":
        print("Iniciando nueva practica de vocabulario...")
    case "repasar":
        print("Abriendo palabras para repasar...")
    case "salir":
        print("Cerrando Language App...")
    case _:
        print(f"Comando {comando} no valido")

print("Match - con condiciones")
puntos = int(input("Incluya puntos de la leccion: "))

match puntos:
    case n if n < 0:
        print(f"{n} no es un puntaje valido")
    case 0:
        print("Debe completar la leccion")
    case n if n % 2 == 0:
        print(f"El puntaje {n} es positivo y par")
    case n:
        print(f"El puntaje {n} es positivo e impar")
