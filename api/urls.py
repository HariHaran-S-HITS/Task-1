from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/create/', views.UserCreate.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('user/update/<int:pk>/', views.UserDelete.as_view()),
    path('user/delete/<int:pk>/', views.UserUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
