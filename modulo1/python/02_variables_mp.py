from types import NoneType

MAX_LECCIONES_DIARIAS = 3
nombre_usuario = "Luis Lazo"
edad_usuario = 28
nivel_ingles = 1.5
curso_activo = True
ultima_leccion = None

print(nombre_usuario, "tipo", type(nombre_usuario))
print(edad_usuario, "tipo", type(edad_usuario))
print(nivel_ingles, "tipo", type(nivel_ingles))
print(curso_activo, "tipo", type(curso_activo))
print(ultima_leccion, "tipo", type(ultima_leccion))

nombre_completo: str = "Luis Lazo"
racha_dias: int = 7
progreso_curso: float = 42.5
practica_activa: bool = True
leccion_pendiente: NoneType = None

print(nombre_completo, "tipo", type(nombre_completo))
print(racha_dias, "tipo", type(racha_dias))
print(progreso_curso, "tipo", type(progreso_curso))
print(practica_activa, "tipo", type(practica_activa))
print(leccion_pendiente, "tipo", type(leccion_pendiente))
