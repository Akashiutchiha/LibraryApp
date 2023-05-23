from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from .serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    data = models.Book.objects.all()
    serializer = BookSerializer(data, many=True)
    return Response(serializer.data)