from django.forms import ModelForm, Textarea, Select
from .models import Book, Users, Comment

class BooksForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','genre','description','writer','price']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'book', 'text')
        widgets = {
            "user": Select(choices=Users.objects.all(), attrs={"class": "form-control"}),
            "advert": Select(choices=Comment.objects.all(), attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control"})
        }

