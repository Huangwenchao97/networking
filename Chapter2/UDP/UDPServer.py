# 演示UDP的套接字编程， 这为服务器端的代码

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 将端口号12000与该服务器的套接字绑定在一起
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
