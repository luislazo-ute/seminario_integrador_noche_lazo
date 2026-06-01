from abc import ABC, abstractmethod


class Actividad(ABC):
    def __init__(self, idioma="ingles"):
        self.idioma = idioma

    @abstractmethod
    def calcular_puntos(self) -> float:
        pass

    @abstractmethod
    def tiempo_estimado(self) -> float:
        pass

    def describir(self) -> str:
        return (
            f"{self.__class__.__name__} de {self.idioma}: "
            f"puntos={self.calcular_puntos():.2f}, "
            f"minutos={self.tiempo_estimado():.2f}"
        )


class Vocabulario(Actividad):
    def __init__(self, palabras, idioma="ingles"):
        super().__init__(idioma)
        self.palabras = palabras

    def calcular_puntos(self):
        return self.palabras * 2

    def tiempo_estimado(self):
        return self.palabras * 0.5


class Escucha(Actividad):
    def __init__(self, audios, idioma="ingles"):
        super().__init__(idioma)
        self.audios = audios

    def calcular_puntos(self):
        return self.audios * 5

    def tiempo_estimado(self):
        return self.audios * 3


class Escritura(Actividad):
    def __init__(self, frases, idioma="ingles"):
        super().__init__(idioma)
        self.frases = frases

    def calcular_puntos(self):
        return self.frases * 4

    def tiempo_estimado(self):
        return self.frases * 2


actividades = [
    Vocabulario(20, "ingles"),
    Escucha(3, "frances"),
    Escritura(5, "portugues"),
]

for actividad in actividades:
    print(actividad.describir())

puntos_total = sum(a.calcular_puntos() for a in actividades)
print(f"Puntos total: {puntos_total:.2f}")
