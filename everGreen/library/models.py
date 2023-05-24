from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    pdf_reference = models.FileField(upload_to='pdfs/', null=True, verbose_name="", storage=FileSystemStorage(location=settings.MEDIA_ROOT))

    def __str__(self):
        return self.title
    
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.username
    
class LibraryCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuedDate = models.DateField(auto_now_add=True)
    returnedDate = models.DateField()
    is_returned = models.BooleanField(default=False)
    cardNumber = models.IntegerField()
    
    def __str__(self):
        return str(self.cardNumber)
    
class Borrowing(models.Model):
    borrowing_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    card_id = models.ForeignKey(LibraryCard, on_delete=models.CASCADE)
    borrowDate = models.DateField(auto_now_add=True)
    date_due = models.DateField()
    is_returned = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.borrowing_id)
    
    
