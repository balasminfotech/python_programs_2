import socket
hostname=socket.gethostname()
print(hostname)
ipAddr=socket.gethostbyname(hostname)
print(ipAddr)