from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('authors',views.authors),
    path('create_book',views.create_book),
    path('create_author',views.create_author),
    path('book/<int:book_id>',views.book),
    path('book/<int:book_id>/assign',views.add_book),
    path('author/<int:author_id>',views.author),
    path('author/<int:author_id>/assign', views.add_author),
]