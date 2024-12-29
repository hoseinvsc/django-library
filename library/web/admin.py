from django.contrib import admin
from .models import Students, Writer, Book, Category, Borrow, Review

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_card', 'phone_number', 'add_time')

class WriterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_year', 'living_place', 'is_dead')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'number_of_pages', 'cover_type', 'printing_time', 'avaliable','category')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class BorrowAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'borrow_date', 'return_date', 'is_returned')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'rating')

admin.site.register(Students, StudentsAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Review, ReviewAdmin)
