# 演示UDP的套接字编程， 这为客户机端的代码
# 《计算机网络自顶向下方法》 P111

from socket import *

serverName = '192.168.1.200'
serverPort = 12000

# 创建客户的TCP套接字
clientSocket = socket(AF_INET, SOCK_STREAM)

# 在客户与服务器之间创建一个TCP连接（执行三次握手）
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentense:')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())

clientSocket.close()
