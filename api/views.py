from rest_framework import generics
from books.models import Books
from .serializers import BooksSerializer


class BooksAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
