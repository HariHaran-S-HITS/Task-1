from .models import User
from .serializers import UserListRetriveSerializer, BookSerializer, UserCreateSerializer
from django.http import Http404
from rest_framework import generics

# create your views here


class UserList(generics.ListAPIView):
    """UserListView."""

    queryset = User.objects.all()
    serializer_class = UserListRetriveSerializer

class UserCreate(generics.CreateAPIView):
    """UserCreate."""

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetail(generics.RetrieveAPIView):
    """UserDetatil."""

    queryset = User.objects.all()
    serializer_class = UserListRetriveSerializer

class UserDelete(generics.DestroyAPIView):
    """UserDelete."""

    queryset = User.objects.all()
    serializer_class = UserListRetriveSerializer


class UserUpdate(generics.UpdateAPIView):
    """UserUpdate."""

    queryset = User.objects.all()
    serializer_class = UserListRetriveSerializer
