from django.urls import path
from . import views 
# primera ruta para la aplicacion 
urlpatterns = [ 
            path('plantilla', views.plantilla, name='plantilla'),
] 
# 127.0.0.1:8000/plantilla