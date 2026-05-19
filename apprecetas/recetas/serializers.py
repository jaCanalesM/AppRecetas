from rest_framework import serializers
from .models import *
from dotenv import load_dotenv
import os


class RecetaSerializer(serializers.ModelSerializer):
    Categoria = serializers.ReadOnlyField(source='categoria.nombre')
    fecha = serializers.DateTimeField(format="%d/%m/%Y")
    imagen = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Receta
        fields = ("id", "nombre", "descripcion", "ingredientes", "pasos", "foto", "Categoria", "fecha", "imagen")
        
    
    def get_imagen(self, obj):
        return f"{os.getenv('BASE_URL')}/media/{obj.foto}"
    
    