# A Simple HTTP Client that communicates with web servers using sockets

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
site = input('Enter site you want to visit: ')
path = input('Enter page path (e.g home): ')

if not path.startswith('/'):
    path = '/' + path

mysock.connect((site, 80))
cmd = f'GET {path} HTTP/1.0\r\nHost: {site}\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
