from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializer import *


{
"username":"neil2",
"password":"123456",
"email":"christiangonore2003@gmail.com"
}

class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
#Register
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
#Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#Book detail
class BookAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(models.Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
#Get all books
class BookListView(APIView):
    def get(self, request):
        books = models.Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)