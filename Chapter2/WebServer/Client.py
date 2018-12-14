# Web服务器编程， 这为客户端的代码
# 《计算机网络自顶向下方法》 P119

from socket import *

serverName = '192.168.1.200'
serverPort = 12000

# 创建客户的TCP套接字
clientSocket = socket(AF_INET, SOCK_STREAM)

# 在客户与服务器之间创建一个TCP连接（执行三次握手）
clientSocket.connect((serverName, serverPort))

sentence = r'GET C:/Users/win7/Desktop/test.html HTTP/1.1' + '\n' + \
           'Host: 192.168.1.200' + '\n' +\
           'Connection: close' + '\n' +\
           'User-agent: Mozilla/5.0' + '\n' +\
           'Accept-language: cn'

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(4096)
print('---------------------------')
print('From Server: ', modifiedSentence.decode())
print('---------------------------')
clientSocket.close()
