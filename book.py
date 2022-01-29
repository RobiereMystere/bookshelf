from author import Author
from database_manager import DatabaseManager
from database_utils import DatabaseUtils
from isbnlib import canonical, meta, desc


class Book:
    isbn: str
    title: str
    book_author_relation_id: int
    description: str
    language: str
    year: int

    def __init__(self, isbn):
        dbu = DatabaseUtils("data/bookshelf.db")

        data = Book.find_by_isbn(isbn)
        self.book_id = 1 + dbu.last_id('book')
        self.isbn = isbn
        self.title = data['Title']
        self.book_author_relation_id = dbu.last_id("book_author_relation") + 1
        print(data)
        for author in data['Authors']:
            dbu.insert('author', [1 + dbu.last_id('author'), Author(author).name])
            dbu.insert('book_author_relation',
                       [self.book_author_relation_id, dbu.cursor.lastrowid,
                        self.book_id])
        self.description = desc(self.isbn)
        self.language = data['Language']
        self.year = data['Year']
        dbu.insert('book',
                   [dbu.last_id("book") + 1, self.isbn, self.title, self.book_author_relation_id, self.description,
                    self.language,
                    self.year])
        dbu.commit()

    @staticmethod
    def find_by_isbn(isbn) -> dict:
        return meta(canonical(isbn))
