"""发送图片附件邮件"""

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
try:
    # 连接到服务器
    smtp = SMTP(host='smtp.163.com')
    useremail = "18137128152@163.com"
    # 登录，   用户名，密码
    smtp.login(useremail, "qikuedu")
    # # 邮件内容  构造发送普通文本邮件对象
    # sendtest = MIMEText("这是一封PYthon写的邮件")
    # 构造发送附件图片对象
    sendtest = MIMEMultipart()
    # 显示谁发的
    sendtest["from"] = useremail
    # 显示发给谁
    sendtest["to"] = '2606662988@qq.com'
    # 邮件主题
    sendtest["subject"] = "PYthon测试邮件"

    # 构造文本对象 添加进邮件对象
    # text = MIMEText("helloworld")
    # sendtest.attach(text)

    # 构造图片对象 添加进邮件对象
    with open("123.jpg", 'rb')as f:
        imgdata = MIMEImage(f.read())
        imgdata.add_header("Content-ID","img001")
        sendtest.attach(imgdata)

    htmlcontent = "<h1>图片</h1><img src='cid:img001/><p>结束</p>"
    html = MIMEText(htmlcontent,'html')
    sendtest.attach(html)

    filedoc = open("demo04.py","rb")
    msgfile = MIMEText(filedoc.read(),"base64","utf-8")
    filedoc.close()
    msgfile["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以随意写，写什么名字，邮件中显示什么名字
    msgfile["Content-Type"] = 'attachement;filename = "test.docx"'
    sendtest.attach(msgfile)

    # 发送方法  第一个参数为发件人   第二个参数为收件人列表   第三个参数为邮件转字符串
    smtp.sendmail(useremail, ['2606662988@qq.com'], sendtest.as_string())
    # 退出链接
    smtp.quit()
except Exception as e:
    print(e)



