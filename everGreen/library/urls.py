from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UserListView.as_view(), name="index" ),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('book/api/<int:pk>/', views.BookAPIView.as_view(), name='book_api'),
    path('book/api/', views.BookListView.as_view(), name='book_api'),
]

