import requests
import multiprocessing
import time
from multiprocessing import Pool,Manager
from threading import Thread
# 单进程
# # 装饰器，加时间
# def timecount(f):
#     def fun(*args):
#         start = time.time()
#         f(*args)
#         end = time.time()
#         print("%s消耗时间%s"%(f.__name__,end-start))
#     return fun
#
#
# @timecount
# def singleprocess(urllist):
#     for u in urllist:
#         resp = requests.get(u)
#         picname = u.split('/')[-1]
#         # print(picname)
#         with open("imgs/%s"%(picname,),"wb")as f:
#             f.write(resp.content)
#
# if __name__ == '__main__':
#     urllist = [
#         'https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg',
#         'https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg',
#     ]
#     # 单线程
#     singleprocess(urllist)


# 单进程，多线程，多进程
# 装饰器，加时间
def timecount(f):
    def fun(*args):
        start = time.time()
        f(*args)
        end = time.time()
        print("%s消耗时间%s"%(f.__name__),end-start)
    return fun

# 单进程
@timecount
def singleprocess(urllist):
    for u in urllist:
       loadsave(u)

def loadsave(urlstr):
    resp = requests.get(urllist)
    # split 切片  以'/'为切片位置，[-1]为切取最后一个 '/' 后的字符串
    picname = urlstr.split('/')[-1]
    # print(picname)
    # wb 把字符串转为二进制模式写入文件夹 imgs/ 内
    with open("imgs/%s" % (picname,), "wb")as f:
        f.write(resp.content)



# 多进程
@timecount
def multiprocess(urllist):
    pool = Pool()
    urlqueue = Manager().Queue()
    for u in urllist:
        urlqueue.put(u)
    while True:
        if not urlqueue.empty():
            urlstr = urlqueue.get()
            pool.apply_async(loadsave,args=(urlstr,))
        else:
            break
    pool.close()
    pool.join()

# 多线程
@timecount
def multithread(urllist):
    threadlist = []
    for u in urllist:
        t = Thread(target=loadsave,args=(u,))
        t.start()
        threadlist.append(t)

    for t in threadlist:
        t.join()

if __name__ == '__main__':
    urllist = [
        'https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg',
    ]
    # 多进程   multi 多     process 进
    multiprocess(urllist)
    #多线程   multi 多    thread 线
    multithread(urllist)
