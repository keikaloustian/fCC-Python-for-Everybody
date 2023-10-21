# TRANSPORT CONTROL PROTOCOL (TCP)
# Built on top of IP (Internet Protocol)
# Assumes IP might lose some data therefore stores and transmits data if it appears to be lost
# Reliable data pipe


# TCP CONNECTIONS AKA SOCKETS
# Internet or network socket is the bi-directional connection between two processes across an internet protocol-based computer network such as the internet. E.g. between a browser and a server.


# PORT NUMBERS
# Application or process-specific communications endpoint akin to phone extension numbers.
# Allows multiple networked applications to coexist on the same server.


# SOCKETS IN PYTHON
import socket

# Create socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make the connection to the desired host and port
mysock.connect(('data.pr4e.org', 80))