from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(10, message="Title must be at least 10 characters long"),
            MaxLengthValidator(50, message="Title must not exceed 50 characters")
        ]
    )
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
   

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
           MinLengthValidator(2, message="Category name must be at least 2 characters long.")
        ]
    )

    def __str__(self):
        return self.name

class ISBN(models.Model):
    isbn_number = models.CharField(max_length=20, unique=True)
    author_title = models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='isbns')
    
    def save(self, *args, **kwargs):
        
        if not self.isbn_number:
            self.isbn_number = str(uuid.uuid4())[:13]
        super().save(*args, **kwargs)
    def __str__(self):
        return self.isbn_number