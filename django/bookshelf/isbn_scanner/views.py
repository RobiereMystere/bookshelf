from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, BookAuthorRelation

# Create your views here.
def index(request):
    authors=Author.objects.all()
    template = loader.get_template('isbn_scanner/index.html')
    context = {'authors': authors,}
    #picture = request.FILES['image']
    return render(request,"isbn_scanner/index.html",context)

