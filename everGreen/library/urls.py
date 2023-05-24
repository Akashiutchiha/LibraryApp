from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path("", views.index, name="index" )
]

router = DefaultRouter()
router.register(r'users', views.UserSerializerViewSet, basename='user')
urlpatterns = urlpatterns + router.urls