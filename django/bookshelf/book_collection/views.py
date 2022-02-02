from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, BookAuthorRelation

# Create your views here.
def index(request):
    books=Book.objects.all()
    template = loader.get_template('book_collection/index.html')
    context = {'books': books,}
    return render(request,"book_collection/index.html",context)


