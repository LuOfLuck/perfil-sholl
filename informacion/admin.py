from django.contrib import admin
from .models import Categoria, Post,Comentario
# Register your models here.

class Admin_categoria(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class Admin_post(admin.ModelAdmin):
    readonly_fields = ('created', 'update') 

class Admin_comentario(admin.ModelAdmin):
    readonly_fields = ('created',)   

admin.site.register(Categoria, Admin_categoria)
admin.site.register(Post, Admin_post)
admin.site.register(Comentario, Admin_comentario)
