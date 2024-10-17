from socket import gethostbyname
from sys import argv
from re import search

reg = r"[a-z]*\.[a-z]*"
if not search(reg, argv[1]):
    print("Invalid domain name!")
    exit()
print(gethostbyname(argv[1]))