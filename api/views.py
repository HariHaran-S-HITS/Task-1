from .models import User
from .serializers import UserSerializer
from django.http import Http404
from rest_framework import generics

# create your views here

class UserView(generics.ListCreateAPIView):
    """User Create, List View."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """User Retrive, Destroy, Update View."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
