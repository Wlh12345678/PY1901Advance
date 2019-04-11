import threading,time
import socket

def reserve():
    """接收"""
    while True:
        time.sleep(0.1)
        result = serversocket.recvfrom(1024)
        print(result[0],result[1])

def send(sc,res):
    """发送"""
    while True:
        info = input("请输入发送内容：").encode("utf8")
        sc.sendto(info, res[1])



if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SEND = ("192.168.12.154", 56000)
    SEND_ADDR = serversocket.bind(SEND)
    result = serversocket.recvfrom(1024)
    print(result[0],result[1])
    t1 = threading.Thread(target=send, args=(serversocket, result))
    t1.start()
    t2 = threading.Thread(target=reserve, args=(serversocket, result))
    t2.start()
    t1.join()
    t2.join()