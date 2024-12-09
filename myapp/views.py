from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje":"Bienvenidos a mi aplicación Django! - Roque Romero"}
    return render(request,"myapp/index.html",context)

def alta(request):
    context={"mensaje":"Ingrese los campos a dar de alta:"}
    return render(request,"myapp/alta.html",context)

def modifica(request):
    context={"mensaje":"Ingrese los campos a modificar"}
    return render(request,"myapp/modifica.html",context)

def elimina(request):
    context={"mensaje":"Ingrese nro. a eliminar"}
    return render(request,"myapp/elimina.html",context)