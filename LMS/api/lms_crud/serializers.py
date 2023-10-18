from rest_framework import serializers
from .models import Book, BorrowingBook, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BorrowingBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowingBook
        fields = '__all__'