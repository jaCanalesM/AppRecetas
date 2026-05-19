from xml.parsers.expat import model

from django.db import models
from autoslug import AutoSlugField

from categorias.models import Categoria

# Create your models here.
class Receta(models.Model):
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, default=1)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    slug = AutoSlugField(populate_from='nombre', unique=True)
    tiempo = models.CharField(max_length=100, null=True)
    foto = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'recetas'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'