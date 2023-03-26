import os
import socket
import re, uuid

print('Hello, ', os.getlogin())
h_name = socket.gethostname()
IP_addrs = socket.gethostbyname(h_name)
print("Host Name is:" + h_name)
print("Computer IP Address is:" + IP_addrs)
print(':'.join(re.findall('..', '%012x' %uuid.getnode())))
