"""
ThreadLocal 可以在线程之间 保持税局的独立
多进程 默认多个进程之间内存独立 需要共享使用Queue
多线程 默认多个线程之前共享内存 需要独立可以使用ThreadLocal
"""

import threading

def thead():
    tlocal.age = 20
    print(tlocal.age)

if __name__ == '__main__':
    tlocal = threading.local()
    tlocal.name = "wlh"
    # print(tlocal.name)


    t1 = threading.Thread(target=thead)









