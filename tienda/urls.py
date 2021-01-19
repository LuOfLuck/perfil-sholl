from django.urls import path
from tienda import views

urlpatterns = [

    path('', views.tienda, name="Tienda"),
    path('compra/<int:id_producto>', views.compra, name="Compra"),
    path('completado/', views.completado, name="Completado")
  
]
