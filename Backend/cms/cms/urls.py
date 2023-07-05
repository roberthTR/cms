from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apiCMS import views

router = routers.DefaultRouter()

router.register('clientes',views.cliente)
router.register('tipoContenido',views.tipoContenido)
router.register('sistemaCMS',views.sistemaCMS)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
