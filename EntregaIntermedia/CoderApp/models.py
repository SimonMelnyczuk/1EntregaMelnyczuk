from django.db import models

# Create your models here.
class Planta(models.Model):
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    deInterior = models.CharField(max_length=40)
    
class Arbol(models.Model):
    #codigo = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    alturaMax = models.IntegerField()

    def __str__(self):             #Con esa funcion puedo ver mas datos desde el admin
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.nombreCientifico,self.alturaMax)

class Cactus(models.Model):
    nombre = models.CharField(max_length=30)
    nombreCientifico = models.CharField(max_length=40)
    diasSinAgua = models.IntegerField()