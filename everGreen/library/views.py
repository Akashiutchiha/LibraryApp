from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, FileResponse
from django.contrib.auth import authenticate, login
from rest_framework import permissions, authentication, viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import models
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializer import *
from datetime import datetime


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
            confirm_password = serializer.validated_data['confirm_password']
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
    
#User detail
class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(models.User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
#Search for books
class BookSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if query:
            books = models.Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Search query parameter "q" is required.'}, status=status.HTTP_400_BAD_REQUEST)


#Borrow
class BorrowingAPIView(APIView):
    def post(self, request):
        serializer = BorrowingSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data['book']
            user = serializer.validated_data['user']
            borrowing = models.Borrowing.objects.create(book=book, user=user)
            borrowing.save()
            return Response({'success': 'Book borrowed successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#
class DownloadBookView(generics.GenericAPIView):
    queryset = models.Book.objects.all()
    serializer_class = DownloadHistorySerializer

    def get(self, request, pk):
        book = get_object_or_404(models.Book, pk=pk)
        file_path = book.pdf_reference.path
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')
        
        # Create a new DownloadHistory object
        data = {
            'user': request.user.id,
            'book': book.book_id,
            'downloaded_at': datetime.now()
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return response

    
    # Get download history for a specific user
class DownloadHistoryView(generics.ListAPIView):
    serializer_class = DownloadHistorySerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return models.DownloadHistory.objects.filter(user=user_id)
    
    