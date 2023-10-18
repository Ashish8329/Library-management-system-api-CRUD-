from django.contrib import admin 

# Register your models here.
from .models import Book,User,BorrowingBook

admin.site.register(BorrowingBook),
admin.site.register(User),
admin.site.register(Book),
