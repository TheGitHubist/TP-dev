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

        if data == b'':
            break

        message = data.decode()
        pseudo = ''

        
        newUsr = False

        if 'Hello|' in message and addr not in CLIENTS :
            print('new user recieved')
            pseudo = message.split('|')[1]
            newUsr = True

        CLIENTS[addr] = {}
        CLIENTS[addr]['w'] = writer
        CLIENTS[addr]['r'] = reader
        CLIENTS[addr]['pseudo'] = pseudo

        for addrs in CLIENTS.keys():
            print(addrs)
            if addrs[0] != addr[0]:
                print(addr)
                if newUsr:
                    CLIENTS[addrs]['w'].write(f"{bcolors.OKBLUE}{pseudo} {bcolors.HEADER} has joined{bcolors.ENDC}".encode())
                    await CLIENTS[addrs]["w"].drain()
                else :
                    messList = message.split("\n")
                    print(messList)
                    if len(messList) > 1:
                        print("more than one")
                        CLIENTS[addrs]['w'].write(f"{bcolors.OKBLUE}{addr[2]} {bcolors.HEADER}:> {messList[0]}{bcolors.ENDC}".encode())
                        await CLIENTS[addrs]["w"].drain()
                        spaces = " " * len(f'{addr[2]}:> ')
                        for line in messList[1:]:
                            CLIENTS[addrs]['w'].write(b"\n")
                            CLIENTS[addrs]['w'].write(f"{spaces} {bcolors.HEADER}{line}{bcolors.ENDC}".encode())
                            await CLIENTS[addrs]["w"].drain()
                    else:
                        print("only one")
                        CLIENTS[addrs]["w"].write(f"{bcolors.OKBLUE}{addr[2]} {bcolors.HEADER}:> {messList[0]}{bcolors.ENDC}".encode())
                        await CLIENTS[addrs]["w"].drain()
                    CLIENTS[addrs]['w'].write(b"\n")
                    await CLIENTS[addrs]["w"].drain()
                    print(f"message {message} from {addr} to {addrs}")
            else:
                print("message not sent to self")

async def main():
    server = await asyncio.start_server(handle_client_msg, '10.1.1.22', 8888)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
