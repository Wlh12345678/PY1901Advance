"""
加锁
"""
import threading, time
def thread1():
    # 锁1 给 线程1 加锁
    lock1.acquire()
    # 使用延迟确保加锁成功
    time.sleep(1)
    # 锁2 给 线程1 加锁
    # 一秒钟后 锁2在线程2 已经加锁成功 此处需要等待线程2 释放资源(解锁)才能加锁     陷入等待
    lock2.acquire()
    print("t21")

def thread2():
    # 锁2加锁
    lock2.acquire()
    time.sleep(2)

    # 一秒钟后 锁1在线程1 已经加锁成功 此处需要等待线程1 释放资源才能加锁
    # 锁1 给 线程1 加锁
    lock1.acquire()
    print("t2")

if __name__ == '__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    # lock = threading.Lock()
    # print("init")
    # lock.acquire()
    # print("lock")
    # lock.release()








