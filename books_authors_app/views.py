from django.shortcuts import render,redirect
from .models import *

def books(request):
    context = {
        "all_books" : Book.objects.all(),
    }
    return render(request, "books.html", context)

def authors(request):
    context = {
        "all_authors" : Author.objects.all(),
    }
    return render(request, "authors.html", context)

def create_book(request):
    title = request.POST['title']
    desc = request.POST['desc']
    Book.objects.create(title=title, desc=desc)
    return redirect("/")

def create_author(request):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=firstName, last_name=lastName, notes=notes)
    return redirect("/authors")

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book_id" : book.id,
        "book_name" : book.title,
        "desc" : book.desc,
        "all_authors_assigned" : book.author.all(),
        "all_authors" : Author.objects.all(),
    }

    return render(request, "book.html",context)

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author_id" : author.id,
        "author_name" : (f"{author.first_name} {author.last_name}"),
        "notes" : author.notes,
        "all_books_assigned" : author.book.all(),
        "all_books" : Book.objects.all(),
    }
    return render(request, "author.html",context)

def add_book(request, book_id):
    author = request.POST['author.id']
    book = Book.objects.get(id=book_id)
    book.author.add(author)
    return redirect(f'/book/{book_id}')

def add_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = request.POST['book.id']
    author.book.add(book)
    return redirect(f'/author/{author_id}')
