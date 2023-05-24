from rest_framework import serializers
from . import models
#for authentication
# from django.contrib.auth.models import User

#User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.User
#         fields = '__all__'
        
class LibraryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LibraryCard
        fields = '__all__'
        
class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowing
        fields = '__all__'
