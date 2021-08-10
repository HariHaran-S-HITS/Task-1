from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# create your views here

class UserView(viewsets.ModelViewSet):
    """UserView."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
