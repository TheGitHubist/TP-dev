import os
from datetime import date 
from datetime import datetime
from sys import argv
from re import search
from socket import gethostbyname
from psutil import net_if_addrs

# Check if the IP address is valid

def is_up(ip):    
    ip_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if not search(ip_pattern, ip):
        return 1, "DOWN ! (wrong ip b!tch)"
    else:
        reponse = os.system(f"ping {ip} > $null")
        if reponse == 0:
            return 0, "UP !"
        else:
            return 0, "DOWN !"

def lookup(doname):
    reg = r"[a-z]*\.[a-z]*"
    if not search(reg, doname):
        return 1, "Invalid domain name!"
    try:
        gethostbyname(doname)
    except:
        return 1, "Domain name does not exist"
    return 0, gethostbyname(doname)

def getIpNetMask():
    overall = net_if_addrs()
    for nics, addrs in overall.items():
        if nics == "Wi-Fi":
            addr = str(addrs[1]).split(", ")[1].split("=")[1].split("'")[1]
            netm = str(addrs[1]).split(", ")[2].split("=")[1].split("'")[1]
            return 3, addr, netm

def changeNetToSlash(netmask):
    slash = 0
    for i in range(4):
        lista = str(bin(int(netmask.split(".")[i]))).split("b")[1]
        for c in lista:
            if c == "1":
                slash += 1
    return slash

def IpCidrAndPossibleAddresses() :
    stat, ip, netmask = getIpNetMask()
    cidr = changeNetToSlash(netmask)
    possibleAddresses = 2 ** (32 - cidr)
    idComp = str(ip) + "/" + str(cidr)
    return 3, idComp

def commandManager():
    res = None
    status = 0
    match argv[1]:
        case "lookup":
            status, res = lookup(argv[2])
        case "ping":
            status, res = is_up(argv[2])
        case "ip":
            if len(argv) == 2:
                status, res = IpCidrAndPossibleAddresses()
            else:
                status, res = 4, "Too many arguments, noob"
        case _:
            status, res = 2, str(argv[1]) + "is not an available command, noob"
    print(res)
    logMaker(status)

def logMaker(status):
    LOGFILE = "C:\\Users\\guill\\AppData\\Local\\Temp"
    mode = 0o733
    try:
        os.mkdir(LOGFILE, mode)
    except FileExistsError:
        pass
    LOGFILE += "\\network-tp3"
    try:
        os.mkdir(LOGFILE, mode)
    except FileExistsError:
        pass
    LOGFILE += "\\network.log"
    mess = ""
    with open(LOGFILE, "a+") as f:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        match status:
            case 0:
                mess = str(today) + " " + str(current_time) + " [INFO] Command " + str(argv[1]) + " called successfully with arguments " + str(argv[2])
            case 1:
                mess = str(today) + " " + str(current_time) + " [ERROR] Command " + str(argv[1]) + " called with bad arguments " + str(argv[2])
            case 2:
                mess = str(today) + " " + str(current_time) + " [ERROR] Command " + str(argv[1]) + " does not exist"
            case 3:
                mess = str(today) + " " + str(current_time) + " [INFO] Command " + str(argv[1]) + " called successfully"
            case 4:
                mess = str(today) + " " + str(current_time) + " [ERROR] Command " + str(argv[2]) + " called with too many arguments"
            case _:
                pass
        f.write(mess)
        
commandManager()