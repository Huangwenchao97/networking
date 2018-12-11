# 客户端ping程序客户机端
# 《计算机网络自顶向下方法》 P119

# 1.ping程序经UDP向目标服务器发送10个ping报文
# 2.当对应的pong报文返回时，打印往返时延(RTT)
# 3.因为UDP是不可靠协议，可能会丢失，所以设置客户等待服务器回答的时间至多为1s
# 4.若1s后还没有收到，客户机假定该分组丢失并打印一条丢失报文

# socket模块集成了Python中所有网络通信的基础
from socket import *
import time

serverName = "192.168.1.200"
serverPort = 12000

# 创建客户的套接字， AF_INET指示了底层网络适用Ipv4， SOCK_DGRAM为该套接字的类型，意味着他是一个UDP套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(10):
    sendtime = time.time()
    message = ('Ping 192.168.1.200 %d %s' % (i + 1, sendtime)).encode()
    try:
        # 将message由字符串转换成字节类型， 发送分组
        clientSocket.sendto(message, (serverName, serverPort))

        # 等待接收来自服务器端的数据， recvfrom(2048)设置缓存长度为2048
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

        rtt = time.time() - sendtime
        print('Sequence %d: Reply from %s  RTT = %.9fs' % (i+1, serverName, rtt))
    except Exception as e:
        print('Sequence %d: Request timed out' % (i + 1))
        print(e)

# 关闭套接字
clientSocket.close()
