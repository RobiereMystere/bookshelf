from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
            db_table = "author"


class Book(models.Model):
    isbn=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    language=models.CharField(max_length=20)
    year=models.IntegerField(default=0)
    add_date = models.DateTimeField('date published')
    def __str__(self):
        return self.isbn+'\t'+self.title
    class Meta:
            db_table = "book"

class BookAuthorRelation(models.Model):
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        author=Author.objects.get(id=self.author_id.id)
        book=Book.objects.get(id=self.book_id.id)
        return str(author)+','+str(book)

    class Meta:
            db_table = "book_author_relation"
