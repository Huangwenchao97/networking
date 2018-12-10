# 演示UDP的套接字编程， 这为服务器端的代码

from socket import *

serverPort = 12000

# 创建客户的TCP套接字
serverSocket = socket(AF_INET, SOCK_STREAM)

# 将服务器端口号与套接字关联起来
serverSocket.bind(('', serverPort))

# 让服务器聆听来自客户端的TCP连接请求
serverSocket.listen(1)

print('The Server is ready to receive')

while True:
    # 调用accept()方法，在服务器中创建了一个名为connectionSocket的新套接字，由特定的客户专用
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
