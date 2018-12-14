# Web服务器编程， 这为服务器端的代码

# 具体要求如下:
# 1.当一个客户（浏览器）联系时创建一个连接套接字
# 2.从这个连接接受HTTP请求
# 3.解释该请求以确定所请求的特定文件
# 4.从服务器的文件系统获得请求的文件
# 5.创建一个由请求的文件组成的HTTP相应报文，报文前面有首部行
# 6.经TCP连接像请求的浏览器发送响应

from socket import *

serverPort = 12000

# 创建客户的TCP套接字
serverSocket = socket(AF_INET, SOCK_STREAM)

# 将服务器端口号与套接字关联起来
serverSocket.bind(('', serverPort))

# 让服务器聆听来自客户端的TCP连接请求
serverSocket.listen(1)

print('The Server is ready to receive')

try:
    while True:
        # 调用accept()方法，在服务器中创建了一个名为connectionSocket的新套接字，由特定的客户专用
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(4096)

            filename = message.split()[1]
            f = open(filename)
            sentence = f.read()
            print(sentence)
            header = 'HTTP/1.1 200 OK\n' \
                     'Connection: close\n' \
                     'Content-Type: text/html; charset=utf-8\n' \
                     'Content-Length: %d\n\n' % (len(sentence))
            modifiedMessage = header + sentence
            connectionSocket.send(modifiedMessage.encode('utf-8'))

            connectionSocket.close()
        except IOError:
            header = ' HTTP/1.1 404 Found'
            connectionSocket.send(header.encode())
        finally:
            connectionSocket.close()
finally:
    serverSocket.close()
