from .models import User
from .serializers import UserSerializer
from django.http import Http404
from rest_framework import generics

# create your views here


class UserList(generics.ListAPIView):
    """UserListView."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    """UserCreate."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """UserView."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    """UserView."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    """UserView."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
