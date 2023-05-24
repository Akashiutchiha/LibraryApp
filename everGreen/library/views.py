from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from .serializer import *

# Create your views here.
# @api_view(['GET'])
# def index(request):
#     data = models.Book.objects.all()
#     serializer = BookSerializer(data, many=True)
#     return Response(serializer.data)


class UserSerializerViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]