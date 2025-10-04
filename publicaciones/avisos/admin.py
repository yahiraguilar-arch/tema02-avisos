from django.contrib import admin
from .models import Aviso

# Register your models here.
@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('aviso', 'fecha_inicio', 'fecha_fin', 'creado')
    list_filter = ('fecha_inicio', 'fecha_fin', 'creado')
    search_fields = ('aviso',)