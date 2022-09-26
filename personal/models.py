from django.db import models

# Create your models here.
class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    fecha_alta = models.DateField(auto_now_add=True)
    
    def nombre_completo(self):
        return f'{self.apellido}, {self.nombre}'

    