#Outgoing Clinet Connection

from socket import *
s = socket(AF_INET,SOCK_STREAM)
host = "192.168.64.1"
port = 9010
s.connect((host,port))
filename = 'Text.txt'
#rb- readonly : Binary
f = open(filename, 'rb')
#1024 BufferSize
l = f.read(1024)
while (l):
    s.send(l)
    print('Sent ', repr(l))
    l = f.read(1024)
f.close()
s.close()

