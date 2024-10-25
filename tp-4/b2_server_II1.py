import socket
import argparse
import sys
import re

host = ''
port = 13337

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-p", "--port", action="store")

parser.add_argument("-l", "--listen", action="store")

parser.add_argument("-h", "--help", action="store_true")
args = parser.parse_args()

if args.help:
    print("Usage: python server.py [options]")
    print("Options:")
    print("-p, --port <port> : Port sur lequel écouter. Par défaut, 13337.")
    print("-l, --listen <adresse> : Adresse IP sur laquelle écouter. Par défaut, toutes les adresses IP disponibles.")
    print("-h, --help : Afficher cette aide.")
    sys.exit(0)

if args.port != None:
    if int(args.port) < 0  or int(args.port) > 65535:
        print(f"ERROR -p argument invalide. Le port spécifié {int(args.port)} n'est pas un port valide (de 0 à 65535).")
        sys.exit(1)
    elif int(args.port) < 1024:
        print(f"ERROR -p argument invalide. Le port spécifié {int(args.port)} est un port privilégié. Spécifiez un port au dessus de 1024.")
        sys.exit(2)
    else:
        port = int(args.port)

if args.listen != None:
    if not re.search('^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$', str(args.listen)):
        print(f"ERROR -l argument invalide. L'adresse {args.listen} n'est pas une addresse valide.")
        sys.exit(3)
    else:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((args.listen, port))
        except socket.error as e:
            print(f"ERROR -l argument invalide. L'adresse {args.listen} n'est pas l'une des adresses IP de cette machine.")
            sys.exit(4)

host = args.listen

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)

while True:

    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        conn.sendall("Hi mate!")

    except socket.error:
        print("Error Occured.")
        break


conn.close()