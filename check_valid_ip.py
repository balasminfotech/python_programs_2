import socket
address='192.168.1.2'
try:
    socket.inet_aton(address)
    print("Valid IP address")
except:
    print("Invalid IP")