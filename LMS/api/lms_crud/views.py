from .models import Book,User,BorrowingBook
from .serializers  import BookSerializer,UserSerializer,BorrowingBookSerializer
# from rest_framework import generics  #using generics 
 


# class Booklist_create_view(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class Book_details_view(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class User_list(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class User_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class BorrowingBook_list(generics.ListCreateAPIView):
#     queryset = BorrowingBook.objects.all()
#     serializer_class = BorrowingBookSerializer


# class BorrowingBook_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BorrowingBook.objects.all()
#     serializer_class = BorrowingBookSerializer


# By using viewset 
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BorrowingBookViewSet(viewsets.ModelViewSet):
    queryset = BorrowingBook.objects.all()
    serializer_class = BorrowingBookSerializer


 


