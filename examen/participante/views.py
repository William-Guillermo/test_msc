from django.shortcuts import render, HttpResponse

# Create your views here.
# Una vez creado las APP  de participante, y garage , 
# python manage.py startapp garage      python manage.py startapp participante
#  Crar las vistas de los templates

def participante_view(request):

    return HttpResponse("Alta de Participante")
