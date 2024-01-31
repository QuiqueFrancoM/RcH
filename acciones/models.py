from django.db import models
class persona(models.Model):
    alias = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    foto = models.ImageField(upload_to='./static/images/personas', null=True, blank=True)
    correo = models.EmailField()
    telefono = models.IntegerField(null=True, blank=True)
    def __str__(self):
        ali = self.nombre + " ("+self.alias+")"
        return ali

class acciones(models.Model):
    titulo = models.CharField(max_length=30)
    origen = models.CharField(max_length=30, null=True)
    creador = models.ForeignKey(persona, on_delete=models.DO_NOTHING, null=True, related_name='creador')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    responsable = models.ForeignKey(persona, on_delete=models.DO_NOTHING, null=True, related_name='responsable')
    descripcion = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='./static/images/acciones', null=True, blank=True)
    def __str__(self):
        return self.titulo