# api/urls.py
# ─────────────────────────────────────────────────────────────────────────
#  Router de DRF: genera automáticamente las rutas CRUD de cada ViewSet.
# ─────────────────────────────────────────────────────────────────────────
from rest_framework.routers import DefaultRouter
from .views import VeterinarioViewSet, MascotaViewSet, CitaViewSet

router = DefaultRouter()
router.register("veterinarios", VeterinarioViewSet)
router.register("mascotas", MascotaViewSet)
router.register("citas", CitaViewSet)

urlpatterns = router.urls
