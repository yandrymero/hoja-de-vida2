from django.shortcuts import render
from .models import Perfil, Curso, Experiencia, ProductoAcademico,ProductoLaboral,Reconocimiento, VentaGaraje


def inicio(request):
    perfil = Perfil.objects.first()
    cursos = Curso.objects.all()
    experiencias = Experiencia.objects.all()
    productos_academicos = ProductoAcademico.objects.all()
    productos_laborales= ProductoLaboral.objects.all()
    reconocimientos = Reconocimiento.objects.all()
    ventas = VentaGaraje.objects.all()

    return render(request, 'inicio.html', {
        'perfil': perfil,
        'cursos': cursos,
        'experiencias': experiencias,
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
        'reconocimientos': reconocimientos,
        'ventas': ventas,
    })
