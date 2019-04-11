# 1.引入socket模块：
from socket import *
# 2.构造服务端socket对象
serversocket = socket(AF_INET, SOCK_DGRAM)
# 3.绑定地址
serversocket.bind(("192.168.12.154", 60000))
result = serversocket.recvfrom(1024)
print(result)
info = input("输入发送信息")
serversocket.sendto(info.encode('utf8'), result[1])


