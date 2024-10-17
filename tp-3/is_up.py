from os import system
from sys import argv
from re import search

# Check if the IP address is valid

ip_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

if not search(ip_pattern, argv[1]):
    print("DOWN ! (wrong ip b!tch)")
else:
    reponse = system(f"ping {argv[1]} > $null")
    if reponse == 0:
        print("UP !")
    else:
        print("DOWN !")