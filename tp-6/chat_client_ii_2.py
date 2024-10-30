import socket
import sys

host = '10.1.1.22'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(b'Hello!')
data = s.recv(1024)

s.close()

print(f"Le serveur a répondu {repr(data)}")
sys.exit(0)