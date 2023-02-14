# se crea un archivo urls.py  por cada aplicacion app  y se relacionara con el urls.py principal del proyecto Examen
# importar path
from django.urls import path

# se manda a traer las vistas de la aplicacion garage
from garage import views

urlpatterns = [
    
    #path('',views.home, name="home"),
    path('', views.home, name="home"),
    path('contratos', views.contratos, name="contratos"),
    path('automovil', views.automovil, name="automovil"),
    path('caracteristicas', views.caracteristicas, name="caracteristicas"),
    path('contacto', views.contacto, name="contacto"),
]
