from django.forms import ModelForm, Textarea, Select
from .models import Book, Comment
from django.contrib.auth import get_user_model
from users.models import Profile


class BooksForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','genre','description','writer','price', 'coverpage']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ( 'book', 'text')
        widgets = {
           # "user": Select(choices=user.objects.all(), attrs={"class": "form-control"}),
            "advert": Select(choices=Comment.objects.all(), attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control"})
        }


