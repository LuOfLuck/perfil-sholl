from django.urls import path
from promociones import views


urlpatterns = [
    path('', views.promociones, name="Promociones"),
    path('egresados/<int:año>/', views.egrasados, name="Egresados"),
    path('recuerdos/<int:año>/', views.recuerdos, name="Recuerdos"),
]

