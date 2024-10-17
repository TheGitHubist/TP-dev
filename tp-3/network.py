import os
import platform
from datetime import date 
from datetime import datetime
from sys import argv
from re import search
from socket import gethostbyname, AddressFamily
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
    comparator = ""
    if platform.system() == "Windows":
        comparator = "Wi-Fi"
    elif platform.system() == "Linux":
        comparator = "enp0s8"
    else:
        pass
    addr, netm = None, None
    for key, value in overall.items():
        if key == comparator:
            for i in range(len(value)):
                if value[i].family == AddressFamily.AF_INET:
                    addr = value[i].address
                    netm = value[i].netmask
                    break
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
    if argv[1] == "lookup":
        status, res = lookup(argv[2])
    elif argv[1] == "ping":
        status, res = is_up(argv[2])
    elif argv[1] == "ip":
        if len(argv) == 2:
            status, res = IpCidrAndPossibleAddresses()
        else:
            status, res = 4, "Too many arguments, noob"
    else:
        status, res = 2, str(argv[1]) + "is not an available command, noob"
    print(res)
    logMaker(status)

def logMaker(status):
    LOGFILE = ""
    if platform.system() == "Windows":
        LOGFILE = "C:\\Users\\guill\\AppData\\Local\\Temp"
    elif platform.system() == "Linux":
        LOGFILE = "/tmp"
    else:
        exit()
    mode = 0o733
    try:
        os.mkdir(LOGFILE, mode)
    except FileExistsError:
        pass
    if platform.system() == "Windows":
        LOGFILE += "\\network-tp3"
    elif platform.system() == "Linux":
        LOGFILE += "/network-tp3"
    else:
        exit()
    try:
        os.mkdir(LOGFILE, mode)
    except FileExistsError:
        pass
    if platform.system() == "Windows":
        LOGFILE += "\\network.log"
    elif platform.system() == "Linux":
        LOGFILE += "/network.log"
    else:
        exit()
    mess = ""
    with open(LOGFILE, "a+") as f:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if status == 0:
            mess = str(today) + " " + str(current_time) + " [INFO] Command " + str(argv[1]) + " called successfully with arguments " + str(argv[2]) + "\n"
        elif status == 1:
            mess = str(today) + " " + str(current_time) + " [ERROR] Command " + str(argv[1]) + " called with bad arguments " + str(argv[2]) + "\n"
        elif status == 2:
            mess = str(today) + " " + str(current_time) + " [ERROR] Command " + str(argv[1]) + " does not exist\n"
        elif status == 3:
            mess = str(today) + " " + str(current_time) + " [INFO] Command " + str(argv[1]) + " called successfully\n"
        elif status == 4:
            mess = str(today) + " " + str(current_time) + " [ERROR] Command " + str(argv[1]) + " called with too many arguments\n"
        else:
            pass
        f.write(mess)
        
commandManager()