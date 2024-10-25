import socket
import sys
import re

host = '10.1.1.22'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

try:
    s.sendall(b'Pack test')
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host, port)

class WrongValueError(Exception):
    pass

message = input('Entrez ce que vous souhaitez envoyer au serveur : ')
if (type(message) != str):
    raise TypeError
elif (not re.search(r'[a-z,A-Z,0-9,\s]*(meo)[a-z,A-Z,0-9,\s]*|[a-z,A-Z,0-9,\s]*(waf)[a-z,A-Z,0-9,\s]*', message)):
    raise WrongValueError("Data not sent, can only send message containing 'meo' or 'waf'. Piece of shit of human !")


s.sendall(message.encode('utf-8'))
data = s.recv(1024)

try:
    print(f"Le serveur a répondu {repr(data)}")
except:
    print("Erreur lors de la réception du message")

s.close()
sys.exit(0)