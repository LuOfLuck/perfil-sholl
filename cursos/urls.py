from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos, name="cursos"),
    path('materias/<int:id_curso>/', views.materia, name="materias"),
]