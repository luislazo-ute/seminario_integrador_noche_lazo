class Estudiante:
    plataforma = "Language App"

    def __init__(self, nombre, edad, idioma):
        self.nombre = nombre
        self.edad = edad
        self.idioma = idioma

    def saludar(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y aprendo {self.idioma}."

    def cambiar_idioma(self, nuevo_idioma):
        self.idioma = nuevo_idioma
        print(f"{self.nombre} ahora practica {self.idioma}.")

    def __str__(self):
        return f"Estudiante({self.nombre}, {self.edad}, {self.idioma})"

    def __repr__(self):
        return f"Estudiante(nombre={self.nombre!r}, edad={self.edad!r}, idioma={self.idioma!r})"


ana = Estudiante("Ana Garcia", 28, "ingles")
luis = Estudiante("Luis Perez", 31, "frances")

print(ana.saludar())
print(luis.saludar())
ana.cambiar_idioma("portugues")
print(str(ana))
print(repr(ana))
print(Estudiante.plataforma)
