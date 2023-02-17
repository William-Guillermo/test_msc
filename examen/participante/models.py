from django.db import models

# Create your models here.

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion=models.CharField(max_length=50,verbose_name="La Direccion")
    telefono=models.CharField(max_length=10)
    email=models.EmailField(blank=True,null=True)  # Dato Opcional (blank=True,null=True
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    
    #imagen_participante = models.ImageField()     pip  install  Pillow    libreria para las imagenes en los modelos del ORM  django
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):

        return self.nombre