from .views import PacienteViewSet, MedicoViewSet, ReservaViewSet
from rest_framework import permissions, routers
from django.urls import path,include

router= routers.DefaultRouter()
router.register(r'paciente', PacienteViewSet)
router.register(r'medico', MedicoViewSet)

router.register(r'reserva', ReservaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]