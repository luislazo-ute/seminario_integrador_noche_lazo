# api/views.py
# ─────────────────────────────────────────────────────────────────────────
#  ViewSets de DRF (equivalente al ejemplo de clase con ModelViewSet).
#  Exponen CRUD completo + búsqueda y ordenamiento; se registran en un router.
#  Incluye una acción personalizada (@action) sobre las citas.
# ─────────────────────────────────────────────────────────────────────────
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Veterinario, Mascota, Cita
from .serializers import (
    VeterinarioSerializer,
    MascotaSerializer,
    CitaSerializer,
)


class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    search_fields = ["nombre", "especialidad", "email"]
    ordering_fields = ["nombre", "creado_en"]


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    search_fields = ["nombre", "dueno", "raza"]
    ordering_fields = ["nombre", "edad", "creado_en"]

    @action(detail=True, methods=["post"])
    def vacunar(self, request, pk=None):
        """Acción personalizada: marca una mascota como vacunada."""
        mascota = self.get_object()
        mascota.vacunado = True
        mascota.save(update_fields=["vacunado"])
        return Response({"id": mascota.id, "nombre": mascota.nombre, "vacunado": True})


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.select_related("mascota", "veterinario").all()
    serializer_class = CitaSerializer
    search_fields = ["motivo", "mascota__nombre", "veterinario__nombre"]
    ordering_fields = ["fecha", "creado_en"]
