from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from . import models
from . import serializers
#media
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime

# Create your views here.

class RecetasView(APIView):
    def get(self, request):
        data = models.Receta.objects.order_by('-id').all()
        datos_json = serializers.RecetaSerializer(data, many=True)
        return JsonResponse({"data": datos_json.data})
    
    def post(self, request):
        if request.data.get("nombre")==None or not request.data["nombre"].strip():
            return JsonResponse({"message": "El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("descripcion")==None or not request.data["descripcion"].strip():
            return JsonResponse({"message": "El campo descripcion es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("ingredientes")==None or not request.data["ingredientes"].strip():
            return JsonResponse({"message": "El campo ingredientes es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("pasos")==None or not request.data["pasos"].strip():
            return JsonResponse({"message": "El campo pasos es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("foto")==None or not request.data["foto"].strip():
            return JsonResponse({"message": "El campo foto es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("categoria")==None or not request.data["categoria"].strip():
            return JsonResponse({"message": "El campo categoria es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        # Validar que la categoria exista
        try:
            categoria = models.Categoria.objects.filter(id=request.data["categoria"]).get()
        except models.Categoria.DoesNotExist:
            return JsonResponse({"message": "La categoria no existe"}, status=HTTPStatus.BAD_REQUEST)
        
        # Validar que no exista una receta con el mismo nombre
        if models.Receta.objects.filter(nombre=request.data["nombre"]).exists():
            return JsonResponse({"message": "Ya existe una receta con ese nombre"}, status=HTTPStatus.BAD_REQUEST)
        
        fs = FileSystemStorage()
        try:
            foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"
        except Exception as e:
            return JsonResponse({"message": "Debe adjuntar una foto"}, status=HTTPStatus.BAD_REQUEST)
        
        try:
            filename = fs.save(foto, request.FILES['file'])
            uploaded_file_url = fs.url(filename)
        except Exception as e:
            return JsonResponse({"message": "Error al guardar la foto"}, status=HTTPStatus.BAD_REQUEST)
        

        try:
            models.Receta.objects.create(nombre=request.data["nombre"], descripcion=request.data["descripcion"], ingredientes=request.data["ingredientes"], pasos=request.data["pasos"], foto=request.data["foto"], categoria_id=request.data["categoria"])
            return JsonResponse({"message": "Receta creada correctamente"}, status=HTTPStatus.CREATED)
        except Exception as e:
            return JsonResponse({"message": "Error al crear la receta"}, status=HTTPStatus.BAD_REQUEST)
    