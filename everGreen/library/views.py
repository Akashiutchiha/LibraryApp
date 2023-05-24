from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import models
from django.contrib.auth.models import User
from .serializer import *

# Create your views here.
# @api_view(['GET'])
# def index(request):
#     data = models.Book.objects.all()
#     serializer = BookSerializer(data, many=True)
#     return Response(serializer.data)

class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
