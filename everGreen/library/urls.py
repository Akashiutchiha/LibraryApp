from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UserListView.as_view(), name="index" )
]

