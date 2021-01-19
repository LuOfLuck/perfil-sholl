from django.urls import path
from sitio_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    path('applica2/', views.applicado2, name="Applica2"),
    path('registrar/', views.Registro_usuarios, name="registro"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)