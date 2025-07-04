from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','categories', 'price', 'published_date']
        widgets = {
           'categories': forms.CheckboxSelectMultiple(),
       }
        execlude = ['user']
        