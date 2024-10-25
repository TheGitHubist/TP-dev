import socket 
import re
import sys

class UnexpactedValueError(Exception):
    pass
class ValueOutOfRangeError(Exception):
    pass

reg = r'[0-9*][\s][+\-*\/][\s][0-9*]|[0-9*][+\-*\/][0-9*]'

def checkMessage(message):
    if type(message) != str:
        raise TypeError("Message must be a string.")
    elif not re.search(reg, message):
        raise UnexpactedValueError("Message does not contain expected expression must be : x operator y ; with x and y integers")
    else:
        value1, value2 = 0, 0
        operator = ""
        if re.search(r'[0-9*][\s][+\-*\/][\s][0-9*]', message):
            value1, operator, value2 = message.split(" ")[0],message.split(" ")[1], message.split(" ")[2]
        else:
            sepMess = []
            for i in range (len(message)):
                if not re.search(r'[0-9]', message[i]):
                    sepMess.append(message[:i])
                elif i == len(message)-1:
                    sepMess.append(message[i+1:])
                    operator = message[i]
            value1, value2 = sepMess[0], sepMess[1]
            if value1 < -1048575 or value2 < -1048575 or value1 > 1048575 or value2 > 1048575:
                raise ValueOutOfRangeError("Values out of range. Can only treat integers between -1048575 and 1048575")
            elif not operator in ["+", "-", "*", "/"]:
                raise UnexpactedValueError("Message does not contain expected operator. Expected operators are +, -, *, /")
            else:
                return message


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

msg = input('Enter a message: ')
try:
    msg = checkMessage(msg)
    print(f'Validated operation: {msg}')
except:
    sys.exit(1)

encoded_msg = msg.encode('utf-8')
msg_len = len(encoded_msg)
header = msg_len.to_bytes(4, byteorder='big')
endline = b'</*-*/>'
payload = header + encoded_msg + endline

sock.send(payload)
sock.close()

sys.exit(0)