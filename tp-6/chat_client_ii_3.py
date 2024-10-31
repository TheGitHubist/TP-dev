import socket
import sys
import aioconsole
import asyncio

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.22',8888))

async def asInput(r, w) :
    while True:
        line = await aioconsole.get_input()
        if line.strip() == 'exit':
            sys.exit(0)
        w.write(line)
        await w.drain()


async def asRecieve(r, w) :
    while True:
        data = await r.read(1024)
        print(data.decode())

        if not data:
            break
        print(f"Le serveur a dit : {data.decode()}")

async def main() :
    reader, writer = await asyncio.open_connection(host="10.1.1.22", port=8888)
    tasks = [asInput(reader, writer), asRecieve(reader, writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    s.close()
    print("Connexion fermee")

sys.exit(0)