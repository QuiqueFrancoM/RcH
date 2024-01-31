from django.db import models

# Create your models here.
class personal(models.Model):
    alias = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    picture = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        ali = self.nombre + " ("+self.alias+")"
        return ali

class globos(models.Model):
    numero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    diam = models.IntegerField(default=10)
    color = models.CharField(max_length=10, default="red")
    def __str__(self):
        globo = str(self.numero) + ".-"+self.nombre
        return globo