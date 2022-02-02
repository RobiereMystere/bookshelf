import socket

from loglib import log

if __name__ == '__main__':
    socket_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_listener.bind(('', 10050))
    socket_listener.listen()
    while True:
        connexion_client, address_client = socket_listener.accept()
        barcode = connexion_client.recv(1024)
        log(connexion_client)
        log(address_client)
        log(barcode)
    socket_listener.close()
