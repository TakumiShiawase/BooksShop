from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Comment
from django.contrib.auth.models import User, auth
from .forms import BooksForm, CommentForm
from .filters import BookFilter
#from users.models import Profile IT WORKS!!!
#from django.contrib.auth.decorators import login_required

class BooksList(ListView):
    model = Book
    template_name = 'store/book_list.html'
    context_object_name = 'book'
    queryset = Book.objects.order_by('-id')

class BooksDetail(DetailView):
    model = Book
    template_name = 'store/book_detail.html'
    context_object_name = 'book_detail'

class BookSearch(ListView):
    template_name = 'store/book_search.html'
    queryset = Book.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context

class BooksCreate(CreateView):
    template_name = 'store/book_create.html'
    form_class = BooksForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BooksForm
        return context


class BooksUpdate(UpdateView):
    template_name = 'store/book_create.html'
    form_class = BooksForm
    success_url = '/'
    queryset = Book.objects.all()


class BooksDelete(DeleteView):
    template_name = 'store/book_delete.html'
    queryset = Book.objects.all()
    success_url = '/'



class CommentView(ListView):
    queryset = Comment.objects.all()
    template_name = 'comment/comment_list.html'

    

class CommentDetailView(DetailView):
    template_name = 'comment/comment_detail.html'


class CommentCreateView(CreateView):
    template_name = 'comment/comment_create.html'
    form_class = CommentForm
    success_url = '/'


class CommentUpdateView(UpdateView):
    template_name = 'comment/comment_create.html'
    form_class = CommentForm

class CommentDeleteView(DeleteView):
    template_name = 'comment/comment_delete.html'
    queryset = Comment.objects.all()
    success_url = '/'

