from book_finder import BookFinder
from isbn_extractor import IsbnExtractor

if __name__ == '__main__':
    all_isbns=IsbnExtractor.extract_from_file("resources/ScannedBooks.csv")
    for isbn in all_isbns:
        BookFinder.find_by_isbn(isbn)
