from django.db import models

 
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BorrowingBook(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s copy of {self.book.title}"


