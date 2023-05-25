from django.contrib import admin
from .models import Book, Comment,Genre

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Genre)