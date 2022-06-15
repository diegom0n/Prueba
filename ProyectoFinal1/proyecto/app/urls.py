from django.urls import path
from.views import home, productos, galeria , agregar_producto, listar_productos, modificar_producto, eliminar_producto, login , registro

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro")
]