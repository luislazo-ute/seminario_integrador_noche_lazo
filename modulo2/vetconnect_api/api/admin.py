# api/admin.py
from django.contrib import admin
from .models import Veterinario, Mascota, Cita


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especialidad", "email", "activo")
    search_fields = ("nombre", "especialidad")


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "raza", "edad", "dueno", "vacunado")
    list_filter = ("especie", "vacunado")
    search_fields = ("nombre", "dueno")


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("mascota", "veterinario", "fecha", "estado")
    list_filter = ("estado",)
