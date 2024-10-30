import socket
import sys

host = '10.1.1.22'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(f"Connecté avec succès au serveur {host} sur le port {port}")

message = input('Entrez ce que vous souhaitez envoyer au serveur : ')
s.sendall(message.encode('utf-8'))
data = s.recv(1024)