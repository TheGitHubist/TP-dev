import sys
import random

def generateId(lenght):
    id = ''
    while lenght > 8:
        comp = 9
        if lenght <= 9:
            comp = lenght
        id += str(hex(random.randrange(1, 10**(comp))))[2:]
        lenght -= 9
    return id

def main():
    print(generateId(int(sys.argv[1])))

if __name__ == "__main__":
    main()