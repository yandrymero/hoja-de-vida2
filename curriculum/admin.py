from django.contrib import admin
from .models import Perfil, Curso, Experiencia, ProductoAcademico, Reconocimiento, VentaGaraje


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'fecha')
    search_fields = ('nombre', 'institucion')


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('puesto', 'empresa', 'fecha')
    search_fields = ('puesto', 'empresa')


@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('titulo','link')
    search_fields = ('titulo',)

from .models import ProductoLaboral


@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    exclude = ('fecha',)
    list_display = ('titulo','link')
    search_fields = ('titulo',)




@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo',)


@admin.register(VentaGaraje)
class VentaGarajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)
