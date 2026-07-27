# api/models.py
# ─────────────────────────────────────────────────────────────────────────
#  MI PROYECTO · VetConnect — Modelos del dominio veterinario
#  Equivale a los modelos del ejemplo de clase (Product/Category/Order),
#  adaptados a VetConnect: Veterinario, Mascota y Cita (con relaciones).
# ─────────────────────────────────────────────────────────────────────────
from django.db import models


class Veterinario(models.Model):
    nombre = models.CharField(max_length=120)
    especialidad = models.CharField(max_length=120, default="General")
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"Dr(a). {self.nombre} — {self.especialidad}"


class Mascota(models.Model):
    class Especie(models.TextChoices):
        PERRO = "PERRO", "Perro"
        GATO = "GATO", "Gato"
        CONEJO = "CONEJO", "Conejo"
        OTRO = "OTRO", "Otro"

    nombre = models.CharField(max_length=120)
    especie = models.CharField(
        max_length=10, choices=Especie.choices, default=Especie.PERRO
    )
    raza = models.CharField(max_length=120, blank=True, default="")
    edad = models.PositiveIntegerField(default=0)
    dueno = models.CharField("Dueño", max_length=120)
    vacunado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.get_especie_display()})"


class Cita(models.Model):
    class Estado(models.TextChoices):
        AGENDADA = "AGENDADA", "Agendada"
        CONFIRMADA = "CONFIRMADA", "Confirmada"
        ATENDIDA = "ATENDIDA", "Atendida"
        CANCELADA = "CANCELADA", "Cancelada"

    mascota = models.ForeignKey(
        Mascota, on_delete=models.CASCADE, related_name="citas"
    )
    veterinario = models.ForeignKey(
        Veterinario, on_delete=models.PROTECT, related_name="citas"
    )
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=12, choices=Estado.choices, default=Estado.AGENDADA
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"Cita {self.mascota.nombre} · {self.fecha:%Y-%m-%d %H:%M}"
