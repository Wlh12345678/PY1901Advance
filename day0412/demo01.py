"""
TCP 客户端
"""
from socket import *
import threading

def tsend(cs):
    try:
        while True:
            to = input("请输入接受用户：")
            message = input("请输入发送消息：")
            if not cs.close:
                cs.send((to+':'+message).encode('gbk'))
            else:
                print("您已经断开连接")
                break
    except Exception as e:
        print(e)

def tread(cs):
    while True:
        result = cs.recv(1024)
        if len(result)>0:
            info = result.decode('gbk').split(':')
            messagefrom = info[0]
            messageinfo = info[1]
            print(messagefrom,':',messageinfo)
        else:
            cs.close()
            break


if __name__ == '__main__':
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("192.168.12.154", 8888))
        username = input("请输入昵称：").encode('gbk')
        client.send(username)

        tr = threading.Thread(target=tread, args=(client,))
        tr.start()
        ts = threading.Thread(target=tsend, args=(client,))
        ts.start()
        tr.join()
        ts.join()
        print("finish")
        client.close()

    except Exception as e:
        print(e)
