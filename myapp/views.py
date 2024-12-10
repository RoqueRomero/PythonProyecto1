from django.shortcuts import redirect,render
from .forms import formulario
from myapp.models import Estudiante

# Create your views here.
def index(request):
    context = {"mensaje":"Bienvenidos a mi aplicación Django! - Roque Romero"}
    return render(request,"myapp/index.html",context)


def alta(request):
    context={"mensaje":"Ingrese los campos a dar de alta:"}
    if request.method=='POST':
        form = formulario(request.POST)
        if form.is_valid():
            form.save()
            context={"mensaje":"Se grabó con éxito"}
            return render(request,"myapp/mensaje.html",context)
    else:
        form=formulario() 
        context={"form":form}
    return render(request,"myapp/alta.html",context)


def lista(request):
    Estudiantes = Estudiante.objects.all()
    context = {'Estudiantes':Estudiantes}
    return render(request,"myapp/lista.html",context)


def busca(request):
    context={"mensaje":"Ingrese nro. a buscar"}
    return render(request,"myapp/busca.html",context)