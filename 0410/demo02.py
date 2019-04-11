import threading

def thread1():
    if lock1.acquire():
        print("1")
        # 在线程1中解锁线程3中的锁
        lock3.release()

def thread2():
    if lock2.acquire():
        print("2")

def thread3():
    # 需要等待lock3 能够加锁  （解锁状态）
    if lock3.acquire():
        print("3")
        lock2.release()

if __name__ == '__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock2.acquire()
    lock3 = threading.Lock()
    lock3.acquire()

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t3 = threading.Thread(target=thread3)

    t1.start()
    t2.start()
    t3.start()





