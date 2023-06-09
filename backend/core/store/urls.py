from django.urls import path
from .views import BooksList, BooksDetail, BooksCreate, BooksUpdate, BooksDelete, CommentView, CommentCreateView, CommentDetailView, BookSearch

urlpatterns = [
    path('', BooksList.as_view()),
    path('<int:pk>', BooksDetail.as_view(), name='book_detail'),
    path('add/', BooksCreate.as_view(), name='book_create'),
    path('<int:pk>/edit/', BooksUpdate.as_view(), name='book_update'),
    path('<int:pk>/delete/', BooksDelete.as_view(), name='book_delete'),
    path('comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment_detail/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment_list/', CommentView.as_view(), name='comment_list'),
    path('search', BookSearch.as_view(), name='book_search'),
    #path('book_favouriteList', BookSearch.as_view(), name='book_search'),

]