from rest_framework.views import APIView
from .models import *
from django.http.response import Http404, HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializers import *
from http import HTTPStatus
from django.utils.text import slugify




# Create your views here.

class CategoriasView(APIView):
    
    
    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriaSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data}, status=HTTPStatus.OK)
    
    
    def post(self, request):
        if request.data.get('nombre') is None or not request.data['nombre']:
            return JsonResponse({"estado":"error","mensaje":"El campo 'nombre' es obligatorio."}, status=HTTPStatus.BAD_REQUEST)
        try:
            Categoria.objects.create(
                nombre=request.data['nombre'])
            return JsonResponse({"estado":"exito","mensaje":"Categoría creada exitosamente."}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
    
    
class Clase2(APIView):
    
    
    def get(self, request, id):
        try:
            data = Categoria.objects.filter(id=id).get()
            return JsonResponse({"data":{"id":data.id, "nombre":data.nombre, "slug":data.slug}}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404("No se encontró la categoría con el id proporcionado.")
    
    
    def put(self, request, id):
        if request.data.get('nombre')==None:
            return JsonResponse({"estado":"error","mensaje":"El campo 'nombre' es obligatorio."}, status=HTTPStatus.BAD_REQUEST)
        if not request.data.get('nombre'):
            return JsonResponse({"estado":"error","mensaje":"El campo 'nombre' es obligatorio."}, status=HTTPStatus.BAD_REQUEST)
        try:
            data=Categoria.objects.filter(id=id).get()
            Categoria.objects.filter(id=id).update(nombre=request.data.get('nombre'), slug=slugify(request.data.get('nombre')))
            return JsonResponse({"estado":"exito","mensaje":"Categoría actualizada exitosamente."}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404("No se encontró la categoría con el id proporcionado.")
        
    
    def delete(self, request, id):
        try:
            data=Categoria.objects.filter(id=id).get()
            Categoria.objects.filter(id=id).delete()
            return JsonResponse({"estado":"exito","mensaje":"Categoría eliminada exitosamente."}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404("No se encontró la categoría con el id proporcionado.")