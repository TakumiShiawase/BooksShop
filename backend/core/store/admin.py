from django.contrib import admin
from .models import Users, Book, Comment,Genre

admin.site.register(Users)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Genre)