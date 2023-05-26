from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UserListView.as_view(), name="index" ),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('book/api/<int:pk>/', views.BookAPIView.as_view(), name='book_api'),
    path('book/api/', views.BookListView.as_view(), name='book_api'),
    path('user/detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('book/search/', views.BookSearchAPIView.as_view(), name='book_search_api'),
    path('borrow/', views.BorrowingAPIView.as_view(), name='book_search_api'),
    path('book/detail/download/<int:pk>/', views.DownloadBookView.as_view(), name='download_book'),
    path('book/history/', views.DownloadBookView.as_view(), name='download_book'),
]

