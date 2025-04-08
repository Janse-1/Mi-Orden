from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaseViewSet, ProyectoViewSet, TareaViewSet, RegistroView

router = DefaultRouter()
router.register(r'clases', ClaseViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tareas', TareaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistroView.as_view(), name='registro'),
]