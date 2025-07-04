from django.contrib import admin
from books.models import Book, Category, ISBN

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(ISBN)

class ISBNInline(admin.StackedInline):
    model = ISBN
    extra = 0
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_date', 'user')
    search_fields = ('title', 'author')
    list_filter = ('published_date', 'categories')
    inlines = [ISBNInline]
    
@admin.register(Category)    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
@admin.register(ISBN)    
class ISBNAdmin(admin.ModelAdmin):
    list_display = ('isbn_number', 'author_title', 'book_title')
    search_fields = ('isbn_number', 'author_title', 'book_title')

