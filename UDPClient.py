import socket

serverName = '127.0.0.2'
serverPort = 16051
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#message = ('abcdefghijklmnopqrstuvwxyz')
message = input('Input lowercase sentance: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()
