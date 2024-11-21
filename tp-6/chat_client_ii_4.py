import socket
import sys
import aioconsole
import asyncio

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.22',8888))

async def asInput(r, w) :
    while True:
        lines = []
        while True:
            ZaLine = await aioconsole.ainput()
            if not ZaLine:
                break
            lines.append(ZaLine)
        line = '\n'.join(lines)
        if line == 'exit':
            sys.exit(0)
        w.write(line.encode())
        await w.drain()


async def asRecieve(r, w) :
    while True:
        data = await r.read(1024)
        if not data:
            break
        print(f"{data.decode()}")

async def main() :
    pseudo = input("Enter your username : ")
    s.sendall(('Hello|' + pseudo).encode())
    reader, writer = await asyncio.open_connection(host="10.1.1.22", port=8888)
    tasks = [asInput(reader, writer), asRecieve(reader, writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    s.close()
    print("Connexion fermee")

sys.exit(0)