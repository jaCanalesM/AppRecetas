from django.urls import path
from .views import *

urlpatterns = [
    path('', RecetasView.as_view()),
]