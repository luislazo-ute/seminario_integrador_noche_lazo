class Recordatorio:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Las subclases deben implementar enviar()")

    def __str__(self):
        return f"{self.__class__.__name__} -> {self.destinatario}"


class RecordatorioEmail(Recordatorio):
    def __init__(self, destinatario, mensaje, asunto="Sin asunto"):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        return f"Email a {self.destinatario}: [{self.asunto}] {self.mensaje}"


class RecordatorioSMS(Recordatorio):
    MAX_CHARS = 160

    def enviar(self):
        msg = self.mensaje[: self.MAX_CHARS]
        return f"SMS a {self.destinatario}: {msg}"


class RecordatorioPush(Recordatorio):
    def enviar(self):
        return f"Push a {self.destinatario}: {self.mensaje[:50]}..."


class RecordatorioChat(Recordatorio):
    def __init__(self, canal, mensaje):
        super().__init__(canal, mensaje)

    def enviar(self):
        return f"Chat #{self.destinatario}: {self.mensaje}"


def notificar_todos(recordatorios: list):
    for recordatorio in recordatorios:
        print(f"  {recordatorio.enviar()}")


alertas = [
    RecordatorioEmail("ana@email.com", "Tu leccion de ingles esta lista", "Practica diaria"),
    RecordatorioSMS("600111222", "Recuerda repasar 10 palabras nuevas"),
    RecordatorioPush("dispositivo-abc", "Nuevo reto de pronunciacion disponible"),
    RecordatorioChat("estudiantes", "Reto grupal de vocabulario iniciado"),
]

print("Enviando recordatorios:")
notificar_todos(alertas)


class ArchivoLocal:
    def leer(self):
        return "progreso desde disco local"

    def escribir(self, datos):
        print(f"Guardando progreso local: {datos[:30]}...")


class ArchivoNube:
    def leer(self):
        return "progreso desde la nube"

    def escribir(self, datos):
        print(f"Subiendo progreso a la nube: {datos[:30]}...")


class ArchivoBD:
    def leer(self):
        return "progreso desde base de datos"

    def escribir(self, datos):
        print(f"Insertando progreso en BD: {datos[:30]}...")


def procesar_archivo(archivo):
    contenido = archivo.leer()
    print(f"Procesando: {contenido}")
    archivo.escribir(f"resultado_{contenido}")


for archivo in [ArchivoLocal(), ArchivoNube(), ArchivoBD()]:
    procesar_archivo(archivo)
