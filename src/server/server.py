from os import execv
import socket
from _thread import *
import sys

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)


s.listen(2)
print("Server started, waiting...")

def threadedClient(connection):
    connection.send(str.encode("Connected!"))
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: "+reply)
            connection.sendall(str.encode(reply))
        except:
            break
    
    print("Dropped Connection")
    connection.close()

while True:
    connection, addr = s.accept()
    print("Connection accepted: ",addr)

    start_new_thread(threadedClient, (connection,))