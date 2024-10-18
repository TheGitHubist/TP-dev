import socket

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()

print("Un client vient de se co et son IP c'est ", addr)

while True:

    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        if (data == "Meo") :
            conn.sendall("Meo a toi cher confrere")
        elif (data == "Waf") :
            conn.sendall("ptdr t ki")
        else:
            conn.sendall("Mes salutations humble humain")

    except socket.error:
        print("Error Occured.")
        break


conn.close()