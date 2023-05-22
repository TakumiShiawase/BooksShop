from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book
from decimal import Decimal
from django.conf import settings

class Favourite(object):
    def favourite_add(request, book.id):
        book = get_object_or_404(Book, id=book.id)
        book.favourite.add(request.user)


def favourite_add(request, book.id):
	favourite = Favourite(request)  
	book = get_object_or_404(Book, id=book.id) 
	favourite.add(book=book)

	return redirect('store/default.html')

def favourite_remove(request, book.id):
    favourite = Favourite(request)  
    book = get_object_or_404(Book, id=book.id)
    favourite.remove(book)
    return redirect('store/favourite_list.html')
