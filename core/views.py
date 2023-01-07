from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
# Create your views here.


def index(request):
    all_books = []

    get_all_books = Book.objects.all()

    return render(request, 'index.html', {'books': get_all_books})

def add(request):
    return render(request, 'add.html')

def insert(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        author = request.POST['author']
        # date = request.POST['date']

        book = Book.objects.create(title=title, desc=desc, author=author)
        book.save()

        return redirect('/')
    return HttpResponse('<h1>Some error occurred...</h1>')

def edit(request):
    book_id = request.GET.get('id')
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        author = request.POST['author']

        book.title = title
        book.desc = desc
        book.author = author
        book.save()
        return redirect('/')
    return render(request, 'edit.html', {'book': book})

def remove(request):
    book_id = request.GET.get('id')
    book = Book.objects.get(id=book_id)

    book.delete()
    return redirect('/')