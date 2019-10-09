#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            sys.stdout.flush()
            print('{}\n'.format(msg))
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    while True:
        msg = input('')
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not HOST:
    HOST = '198.21.229.137'
if not PORT:
    PORT = 44000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

send_thread = Thread(target=send)
send_thread.start()

# tkinter.mainloop()  # Starts GUI execution.
