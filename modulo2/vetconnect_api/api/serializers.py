# api/serializers.py
# ─────────────────────────────────────────────────────────────────────────
#  Serializers de DRF (equivalente al ejemplo de clase con ModelSerializer).
#  Incluye campos calculados/derivados y relaciones anidadas.
# ─────────────────────────────────────────────────────────────────────────
from rest_framework import serializers
from .models import Veterinario, Mascota, Cita


class VeterinarioSerializer(serializers.ModelSerializer):
    total_citas = serializers.IntegerField(source="citas.count", read_only=True)

    class Meta:
        model = Veterinario
        fields = [
            "id", "nombre", "especialidad", "email",
            "activo", "total_citas", "creado_en",
        ]


class MascotaSerializer(serializers.ModelSerializer):
    especie_nombre = serializers.CharField(
        source="get_especie_display", read_only=True
    )

    class Meta:
        model = Mascota
        fields = [
            "id", "nombre", "especie", "especie_nombre", "raza",
            "edad", "dueno", "vacunado", "creado_en",
        ]

    def validate_edad(self, value):
        if value > 40:
            raise serializers.ValidationError("La edad no parece válida para una mascota.")
        return value


class CitaSerializer(serializers.ModelSerializer):
    # Relaciones legibles (solo lectura) + ids para escritura
    mascota_nombre = serializers.CharField(source="mascota.nombre", read_only=True)
    veterinario_nombre = serializers.CharField(source="veterinario.nombre", read_only=True)
    estado_nombre = serializers.CharField(source="get_estado_display", read_only=True)

    class Meta:
        model = Cita
        fields = [
            "id", "mascota", "mascota_nombre",
            "veterinario", "veterinario_nombre",
            "fecha", "motivo", "estado", "estado_nombre", "creado_en",
        ]
