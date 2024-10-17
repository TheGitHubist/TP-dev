from psutil import net_if_addrs

def getIpNetMask():
    overall = net_if_addrs()
    for nics, addrs in overall.items():
        if nics == "Wi-Fi":
            addr = str(addrs[1]).split(", ")[1].split("=")[1].split("'")[1]
            netm = str(addrs[1]).split(", ")[2].split("=")[1].split("'")[1]
            return [addr, netm]

def changeNetToSlash(netmask):
    slash = 0
    for i in range(4):
        lista = str(bin(int(netmask.split(".")[i]))).split("b")[1]
        for c in lista:
            if c == "1":
                slash += 1
    return slash

def IpCidrAndPossibleAddresses() :
    ip, netmask = getIpNetMask()
    cidr = changeNetToSlash(netmask)
    possibleAddresses = 2 ** (32 - cidr)
    print(f"{ip}/{cidr}")
    print(f"Possible addresses: {possibleAddresses}")

IpCidrAndPossibleAddresses()