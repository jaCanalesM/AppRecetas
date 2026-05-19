from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from . import models
from . import serializers

# Create your views here.

class RecetasView(APIView):
    def get(self, request):
        data = models.Receta.objects.order_by('-id').all()
        datos_json = serializers.RecetaSerializer(data, many=True)
        return JsonResponse({"data": datos_json.data})