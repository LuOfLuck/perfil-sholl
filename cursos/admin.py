from django.contrib import admin
from .models import Cursos, Materia
# Register your models here.
class CursosAdmin(admin.ModelAdmin):
    list_display = ("año", "especialidad", )
    search_fields = ("especialidad",)
    class Meta:
        ordering = ['año']
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo",)
    search_fields = ("nombre",)
    class Meta:
        ordering = ['nombre'] # ['-name'] if you want the opposite ordering


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Materia, MateriaAdmin)