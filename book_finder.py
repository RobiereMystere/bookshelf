from isbnlib import canonical, meta


class BookFinder:
    @staticmethod
    def find_by_isbn(isbn):
        data = meta(canonical(isbn))
        print(data)
