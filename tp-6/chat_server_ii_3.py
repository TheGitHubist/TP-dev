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

async def handle_client_msg(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        message = data.decode()
        if "\n" in message:
            lines = message.split("\n")
            print(f"{bcolors.OKBLUE}{addr[0]}:{bcolors.OKGREEN}{addr[1]!r} {bcolors.HEADER}:> {lines[0]!r}{bcolors.ENDC}")
            spaces = " " * len(f'{addr[0]!r}:{addr[1]!r}:> ')
            for line in lines[1:]:
                print(f"{spaces} {bcolors.HEADER}{line[1:len(lines)-1]!r}{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKBLUE}{addr[0]!r}:{bcolors.OKGREEN}{addr[1]!r} {bcolors.HEADER}:> {message!r}{bcolors.ENDC}")

        await writer.drain()

async def main():
    server = await asyncio.start_server(handle_client_msg, '10.1.1.22', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
