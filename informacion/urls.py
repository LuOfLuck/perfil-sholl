from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.informacion, name="Informacion"),
    path('categoria/<int:categoria_id>/', views.categoria, name="Categoria"),
    path('post/<int:post_id>/', views.post, name="post"),
]
