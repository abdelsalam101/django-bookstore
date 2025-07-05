from django.urls import path
from django.contrib import admin
from . import views

app_name = 'books'
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]