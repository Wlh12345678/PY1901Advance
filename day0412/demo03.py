"""连接FTP服务器"""
# 1.导入模块
from ftplib import FTP

try:
    ftp = FTP(host='192.168.12.154')

    ftp.login(user='ftpzzy',passwd='123456')

    print(ftp.pwd())
    print(ftp.dir())
    # 5.退出
    ftp.quit()
except Exception as e:
    print(e)


