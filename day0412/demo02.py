"""
TCP 服务端
"""
from socket import *
import threading

def tread(cs,un):
    while True:
        result = cs.recv(1024)
        if len(result) > 0:
            info = result.decode('gbk').split(":")
            to = info[0]
            message = info[1]
            print(to, message)

            if to == "all":
                for u in userdict.keys():
                    if un != u:
                        userdict[u].send(un+':'+message).encode('gbk')
            else:
                if to in userdict.keys():
                    userdict[to].send(un+":"+message).encode('gbk')
                else:
                    cs.send("对方已离线，不能接受消息".encode('gbk'))
        else:
            cs.close()
            userdict.pop(un)
            break


def tlisten(s):
    while True:
        client,clientaddr = s.accept()
        username = client.recv(1024).decode('gbk')
        userdict[username] = client
        print("用户",username,"连接上了 共有用户",len(userdict))

        tr = threading.Thread(target=tread,args=(client, username))
        tr.start()

def tsend():
    while True:
        info = input("请输入通知").encode("gbk")
        for k,v in userdict.items():
            v.send(info)


if __name__ == '__main__':
    userdict = {}
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("192.168.12.154",8888))
    server.listen(20)
    print("开启监听")

    t1 = threading.Thread(target=tread,args=(server,))
    t1.start()

    ts = threading.Thread(target=tsend)
    ts.start()






