from django.contrib import admin
from .models import Author,Book,BookAuthorRelation

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthorRelation)
