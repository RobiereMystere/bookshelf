from book import Book
from database_manager import DatabaseManager
from isbn_extractor import IsbnExtractor

if __name__ == '__main__':
    dmc = DatabaseManager()
    books = []
    all_isbns = IsbnExtractor.extract_from_file("resources/ScannedBooks.csv")
    for isbn in all_isbns:
        books.append(Book(isbn))
        print(books[-1])
    """
    """
