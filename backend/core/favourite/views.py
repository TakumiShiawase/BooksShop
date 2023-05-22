from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book
from decimal import Decimal
from django.conf import settings

class Favourite(object):
    def favourite_add(request, bookid):
        book = get_object_or_404(Book, id=bookid)
        book.favourite.add(request.user)


def cart_add(request, bookid):
	favourite = Favourite(request)  
	book = get_object_or_404(Book, id=bookid) 
	favourite.add(book=book)

	return redirect('store/default.html')

def cart_remove(request, bookid):
    favourite = Favourite(request)  
    book = get_object_or_404(Book, id=bookid)
    favourite.remove(book)
    return redirect('store/favourite_list.html')