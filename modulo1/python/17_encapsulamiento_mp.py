class PerfilIdioma:
    def __init__(self, usuario, puntos_iniciales=0):
        self.usuario = usuario
        self.__puntos = puntos_iniciales
        self.__historial = []
        self.__activo = True
        self.__registrar(f"Perfil creado con {puntos_iniciales} puntos")

    @property
    def puntos(self):
        return self.__puntos

    @property
    def activo(self):
        return self.__activo

    @property
    def historial(self):
        return list(self.__historial)

    def ganar_puntos(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__puntos += cantidad
        self.__registrar(f"Puntos ganados: +{cantidad}")
        return self

    def usar_puntos(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__puntos:
            raise ValueError(f"Puntos insuficientes (disponible: {self.__puntos})")
        self.__puntos -= cantidad
        self.__registrar(f"Puntos usados: -{cantidad}")
        return self

    def compartir_puntos(self, destino, cantidad):
        self.usar_puntos(cantidad)
        destino.ganar_puntos(cantidad)
        self.__registrar(f"Puntos compartidos con {destino.usuario}: -{cantidad}")
        return self

    def __registrar(self, operacion):
        from datetime import datetime

        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial.append(f"[{hora}] {operacion}")

    def __str__(self):
        return f"PerfilIdioma({self.usuario}: {self.__puntos} puntos)"


p1 = PerfilIdioma("Ana Garcia", 1000)
p2 = PerfilIdioma("Luis Perez", 500)

p1.ganar_puntos(500).usar_puntos(200)
p1.compartir_puntos(p2, 300)

print(p1)
print(p2)
print(f"Puntos Ana: {p1.puntos}")

for entrada in p1.historial:
    print(f"  {entrada}")
