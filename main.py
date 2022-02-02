from isbnlib import is_isbn13
from book import Book
import socket


if __name__ == '__main__':

    socket_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        socket_listener.bind(('', 10050))
        socket_listener.listen()

        while True:
            connexion_client, address_client = socket_listener.accept()
            barcode = connexion_client.recv(1024)
            if is_isbn13(str(barcode)):
                book = Book(barcode.decode("utf-8"))
                print(book.title)
    finally:
        socket_listener.close()
