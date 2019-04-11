# 1.引入socket模块
import socket,time
# 2.构造socket对象
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 定义常量用大写
ADDRESS_TO = ('127.0.0.1',60000)
BUFFER_SIZE = 1024

# 3.发送消息
# while True:
#     time.sleep(1)
#     # 发送时一定要指明发送对象
#     clientsocket.sendto("hello".encode("utf8"),ADDRESS_TO)

clientsocket.sendto("hello".encode("utf8"),ADDRESS_TO)

while True:
    info,addr = clientsocket.recvfrom(BUFFER_SIZE)
    print("收到",info)
    print(addr)





