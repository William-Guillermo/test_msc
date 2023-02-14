from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    #return HttpResponse("Contratos")
    return render(request, "garage/home.html")

def contratos(request):

    #return HttpResponse("Contratos")
    return render(request, "garage/contratos.html")

def automovil(request):

    #return HttpResponse("Automovil")
    return render(request, "garage/automovil.html")

def caracteristicas(request):

    #return HttpResponse("Caracterirsticas Automovil")
    return render(request, "garage/caracteristicas.html")

def contacto(request):

    #return HttpResponse("Caracterirsticas Automovil")
    return render(request, "garage/contacto.html")


