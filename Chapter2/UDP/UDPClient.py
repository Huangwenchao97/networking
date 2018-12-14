# 演示UDP的套接字编程， 这为客户机端的代码
# 《计算机网络自顶向下方法》 P106

# 1.客户从其键盘读取一行字符（数据）并将该数据向服务器发送
# 2.服务器接收该数据并将这些字符转换成大写
# 3.服务器将修改的数据发送给客户
# 4.客户接受修改的数据并在其监视器上显示出来

# socket模块集成了Python中所有网络通信的基础
from socket import *


serverName = "192.168.1.200"
serverPort = 12000

# 创建客户的套接字， AF_INET指示了底层网络适用Ipv4， SOCK_DGRAM为该套接字的类型，意味着他是一个UDP套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentense:')

# 将message由字符串转换成字节类型， 发送分组
clientSocket.sendto(message.encode(), (serverName, serverPort))

# 等待接收来自服务器端的数据， recvfrom(2048)设置缓存长度为2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

# 关闭套接字
clientSocket.close()
