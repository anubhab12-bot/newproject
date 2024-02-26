from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSErializer

# Create your views here.
class BookListView(ListAPIView):
    # querySet = Book.objects.all()
    serializer_class = BookSErializer
    
    def get_queryset(self):
        return Book.objects.all()
    
