from author import Author
from database_utils import DatabaseUtils
from isbnlib import canonical, meta, desc


class Book:
    isbn: str
    title: str
    book_author_relation_id: int
    description: str
    language: str
    year: int
    authors: list

    def __init__(self, isbn):
        dbu = DatabaseUtils("data/bookshelf.db")
        data_book = dbu.select_one('book', '*', "isbn = " + isbn)
        self.authors = []
        if data_book is None:
            data = Book.find_by_isbn(isbn)
            self.book_id = 1 + dbu.last_id('book')
            self.isbn = isbn
            self.title = data['Title']
            self.book_author_relation_id = dbu.last_id("book_author_relation") + 1
            for author in data['Authors']:
                t_author = author
                if len(t_author) > 0 and t_author[-1] == ',':
                    t_author = t_author[:-1]

                author_id = dbu.select_one('author', column='id', where='name = "' + t_author + '"')
                if author_id is None:
                    dbu.insert('author', [1 + dbu.last_id('author'), t_author])
                    author_id = dbu.cursor.lastrowid
                else:
                    author_id = author_id[0]
                dbu.insert('book_author_relation',
                           [self.book_author_relation_id, author_id,
                            self.book_id])
            self.description = desc(self.isbn)
            self.language = data['Language']
            self.year = data['Year']
            dbu.insert('book',
                       [dbu.last_id("book") + 1, self.isbn, self.title, self.book_author_relation_id, self.description,
                        self.language,
                        self.year])
            dbu.commit()
        else:
            self.book_id = data_book[0]
            self.isbn = data_book[1]
            self.title = data_book[2]
            self.book_author_relation_id = data_book[3]
            author_ids = dbu.select('book_author_relation', 'author_id', 'id = ' + str(self.book_author_relation_id))
            for author_id in author_ids:
                author_tuple = dbu.select_one('author', '*', 'id = ' + str(author_id[0]))
                self.authors.append(Author(author_tuple[0], author_tuple[1]))
            self.description = data_book[4]
            self.language = data_book[5]
            self.year = data_book[6]

    def __str__(self):
        r = "ID : \t" + str(self.book_id) + "\n"
        r += "ISBN : \t" + self.isbn + "\n"
        r += "Title : \t" + self.title + "\n"
        r += "Authors : \n"
        for author in self.authors:
            r += "\t" + str(author) + "\n"
        r += "Description : \t" + self.description + "\n"
        r += "Language : \t" + self.language + "\n"
        r += "Year : \t" + str(self.year)
        return r

    @staticmethod
    def find_by_isbn(isbn) -> dict:
        return meta(canonical(isbn))
