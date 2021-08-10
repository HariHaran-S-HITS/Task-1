from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Model
from .serializers import ModelSerializer

# create your views here

class ModelView(viewsets.ModelViewSet):
    """ModelView."""

    queryset = Model.objects.all()
    serializer_class = ModelSerializer
