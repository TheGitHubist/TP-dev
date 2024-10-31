import asyncio
global CLIENTS
CLIENTS = {}

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

async def handle_client_msg(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')
        CLIENTS[addr] = {}
        CLIENTS[addr]['w'] = writer
        CLIENTS[addr]['r'] = reader

        if data == b'':
            break

        message = data.decode()
        for addrs in CLIENTS.keys():
            if addrs != addr:
                if "\n" in message:
                    lines = message.split("\n")
                    print(f"{bcolors.OKBLUE}{addr[0]}:{bcolors.OKGREEN}{addr[1]} {bcolors.HEADER}:> {lines[0]}{bcolors.ENDC}")
                    addrs['w'].write(f"{bcolors.OKBLUE}{addr[0]}:{bcolors.OKGREEN}{addr[1]} {bcolors.HEADER}:> {lines[0]}{bcolors.ENDC}".encode())
                    spaces = " " * len(f'{addr[0]}:{addr[1]}:> ')
                    for line in lines[1:]:
                        print(f"{spaces} {bcolors.HEADER}{line}{bcolors.ENDC}")
                        addrs['w'].write(f"{spaces} {bcolors.HEADER}{line}{bcolors.ENDC}".encode())
                else:
                    print(f"{bcolors.OKBLUE}{addr[0]}:{bcolors.OKGREEN}{addr[1]} {bcolors.HEADER}:> {message}{bcolors.ENDC}")
                    addrs["w"].write(f"{bcolors.OKBLUE}{addr[0]}:{bcolors.OKGREEN}{addr[1]} {bcolors.HEADER}:> {message}{bcolors.ENDC}".encode())
                print("\n")

        await writer.drain()

async def main():
    server = await asyncio.start_server(handle_client_msg, '10.1.1.22', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
