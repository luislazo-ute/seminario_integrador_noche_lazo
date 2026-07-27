# api/management/commands/seed.py
# ─────────────────────────────────────────────────────────────────────────
#  Comando de datos de demostración:  python manage.py seed
# ─────────────────────────────────────────────────────────────────────────
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from api.models import Veterinario, Mascota, Cita


class Command(BaseCommand):
    help = "Carga datos de demostración de VetConnect"

    def handle(self, *args, **options):
        Cita.objects.all().delete()
        Mascota.objects.all().delete()
        Veterinario.objects.all().delete()

        vets = [
            Veterinario.objects.create(nombre="Laura Mendoza", especialidad="Cirugía", email="laura@vetconnect.com"),
            Veterinario.objects.create(nombre="Diego Torres", especialidad="Dermatología", email="diego@vetconnect.com"),
            Veterinario.objects.create(nombre="Ana Salas", especialidad="General", email="ana@vetconnect.com"),
        ]

        mascotas = [
            Mascota.objects.create(nombre="Firulais", especie="PERRO", raza="Labrador", edad=3, dueno="Ana García", vacunado=True),
            Mascota.objects.create(nombre="Michi", especie="GATO", raza="Siamés", edad=2, dueno="Luis Pérez"),
            Mascota.objects.create(nombre="Rocky", especie="PERRO", raza="Bulldog", edad=5, dueno="María López", vacunado=True),
            Mascota.objects.create(nombre="Nube", especie="CONEJO", raza="Angora", edad=1, dueno="Carlos Ruiz"),
            Mascota.objects.create(nombre="Pelusa", especie="GATO", raza="Persa", edad=6, dueno="Jorge Mora", vacunado=True),
        ]

        ahora = timezone.now()
        Cita.objects.create(mascota=mascotas[0], veterinario=vets[0], fecha=ahora + timedelta(days=1), motivo="Control anual", estado="CONFIRMADA")
        Cita.objects.create(mascota=mascotas[1], veterinario=vets[1], fecha=ahora + timedelta(days=2), motivo="Revisión de piel", estado="AGENDADA")
        Cita.objects.create(mascota=mascotas[2], veterinario=vets[2], fecha=ahora + timedelta(days=3), motivo="Vacunación", estado="AGENDADA")
        Cita.objects.create(mascota=mascotas[3], veterinario=vets[0], fecha=ahora - timedelta(days=1), motivo="Corte de uñas", estado="ATENDIDA")

        self.stdout.write(self.style.SUCCESS(
            f"Datos cargados: {Veterinario.objects.count()} veterinarios, "
            f"{Mascota.objects.count()} mascotas, {Cita.objects.count()} citas."
        ))
