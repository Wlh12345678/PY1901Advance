import threading
import socket

def send(sc,sendto):
    while True:
        info = input("请输入发送内容：").encode("utf8")
        sc.sendto(info,sendto)

def recv(sc,buffersize):
    while True:
        info,addr = sc.recvfrom(buffersize)
        print(info.decode('utf8'),addr)

if __name__ =="__main__":
    # main()

    SEND_ADDR = ('192.168.12.154',60000)
    BUFFER_SIZE = 1024
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientSocket.sendto("hello".encode("utf-8"), SEND_ADDR)
    t1 = threading.Thread(target=send, args=(clientSocket,SEND_ADDR))
    t1.start()
    t2 = threading.Thread(target=recv, args=(clientSocket,BUFFER_SIZE))
    t2.start()
    t1.join()
    t2.join()


