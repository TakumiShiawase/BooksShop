from django.shortcuts import render
from django.db.models import Q
from store.models import Book

def search(request):
	search = request.GET.get('q')
	books = Book.objects.all()
	if search:
		books = books.filter(
			Q(name__icontains=search)|Q(genre__name__icontains=search)|Q(writer__name__icontains=search)

		)

