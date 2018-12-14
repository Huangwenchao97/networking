# 创建一个向任何接收方发送电子邮件的简单右键客户

# 1.与邮件服务器创建一个TCP连接
# 2.使用STMP协议与邮件服务器进行交谈
# 3.经该邮件服务器对接收方发送一个电子邮件报文
# 4.关闭TCP连接

from socket import *


def receiveFromServer():
    msg = clientSocket.recv(1024).decode()
    print(msg)
    return msg


# qq邮箱SMTP服务器，端口25
serverName = 'smtp.163.com'
serverPort = 25

# 需要在内容开始部分加msg， 在结束部分加endmsg
msg = b"Who are you?\r\n"
endmsg = b"\r\n.\r\n"


# 创建客户的TCP套接字
clientSocket = socket(AF_INET, SOCK_STREAM)

# 在客户与服务器之间创建一个TCP连接（执行三次握手）
clientSocket.connect((serverName, serverPort))

heloCommand = 'HELO doocter\r\n'
clientSocket.sendall(heloCommand.encode())
receiveFromServer()

# 登录命令
loginCommand = 'AUTH LOGIN\r\n'

# 邮箱账号的base64编码
addr = 'bTE4NzkyNTU2MzYxQDE2My5jb20=\r\n'
# 用户名的base64编码
username = 'SFdjaGFv\r\n'
# 授权码的base64编码
passwd = 'ZG9vY3RlcjAwNw==\r\n'

# 登录服务
clientSocket.sendall(loginCommand.encode())
receiveFromServer()
clientSocket.send(addr.encode())
receiveFromServer()
clientSocket.sendall(passwd.encode())
receiveFromServer()


sendaddr = 'mail from: <18792556361@163.com>\r\n'
recaddr = 'rcpt to: <2248872886@qq.com>\r\n'
data = 'data\r\n'

# 发送邮件
clientSocket.sendall(sendaddr.encode())
receiveFromServer()
clientSocket.sendall(recaddr.encode())
receiveFromServer()
clientSocket.sendall(data.encode())
clientSocket.recv(1024)

clientSocket.sendall(b'from:18792556361@163.com\r\n')
clientSocket.sendall(b'to:2248872886@qq.com\r\n')
clientSocket.sendall(b'subject:kuku is smart\r\n')
clientSocket.sendall(b'Content-Type:text/plain\t\n')
clientSocket.sendall(b'\r\n')
clientSocket.sendall(msg)
clientSocket.sendall(endmsg)
receiveFromServer()

# 退出连接
clientSocket.sendall(b'quit\r\n')
receiveFromServer()

clientSocket.close()
