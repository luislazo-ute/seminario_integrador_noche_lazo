class Curso:
    def __init__(self, idioma, nivel, anio):
        self.idioma = idioma
        self.nivel = nivel
        self.anio = anio
        self._progreso = 0

    def avanzar(self, incremento):
        self._progreso = min(100, self._progreso + incremento)
        return self

    def repasar(self, decremento):
        self._progreso = max(0, self._progreso - decremento)
        return self

    def __str__(self):
        return f"{self.idioma} {self.nivel} ({self.anio}) - {self._progreso}%"


class CursoVocabulario(Curso):
    def __init__(self, idioma, nivel, anio, palabras=100):
        super().__init__(idioma, nivel, anio)
        self.palabras = palabras

    def practicar(self):
        return f"{self.idioma} {self.nivel}: practicando vocabulario"

    def __str__(self):
        return f"{super().__str__()} ({self.palabras} palabras)"


class CursoPronunciacion(Curso):
    def __init__(self, idioma, nivel, anio, audios):
        super().__init__(idioma, nivel, anio)
        self.audios = audios

    def grabar_audio(self):
        return f"{self.idioma}: grabando pronunciacion"

    def __str__(self):
        return f"{super().__str__()} ({self.audios} audios)"


class CursoPremium(CursoVocabulario):
    def __init__(self, idioma, nivel, anio, palabras, tutorias):
        super().__init__(idioma, nivel, anio, palabras)
        self.__tutorias = tutorias
        self.__tutorias_usadas = 0

    def usar_tutoria(self, cantidad=1):
        self.__tutorias_usadas = min(self.__tutorias, self.__tutorias_usadas + cantidad)
        return self

    @property
    def tutorias_restantes(self):
        return self.__tutorias - self.__tutorias_usadas

    def __str__(self):
        return f"{super().__str__()} | Tutorias restantes: {self.tutorias_restantes}"


ingles = CursoPremium("Ingles", "B1", 2026, 500, 8)
ingles.avanzar(45)
print(ingles)

print(isinstance(ingles, CursoPremium))
print(isinstance(ingles, CursoVocabulario))
print(isinstance(ingles, Curso))
print(isinstance(ingles, CursoPronunciacion))

print(CursoPremium.__mro__)
