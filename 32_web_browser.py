import socket

print('Initializing simple web browser\n')

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/2.0\r\n\r\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end='')
my_socket.close()

print('Done')