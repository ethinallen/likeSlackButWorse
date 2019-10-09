from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print(host)
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

print('Waiting for connection.')

while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   message = 'Thank you for connecting'
   c.send(message.encode('utf-8'))
   c.close()                # Close the connection

def acceptConnections():
    while True:
        client, clientAddress = SERVER.accept()
        print('%s:%s has connected.' % clientAddress)
