"""发送普通邮件"""

from smtplib import SMTP
from email.mime.text import MIMEText

try:
    # 连接到服务器
    smtp = SMTP(host='smtp.163.com')
    useremail = "18137128152@163.com"
    # 登录，   用户名，密码
    smtp.login(useremail,"qikuedu")
    # 邮件内容  构造发送普通文本邮件对象
    sendtest = MIMEText("这是一封PYthon写的邮件")
    # 显示谁发的
    sendtest["from"] = useremail
    # 显示发给谁
    sendtest["to"] = '2606662988@qq.com'
    # 邮件主题
    sendtest["subject"] = "PYthon测试邮件"


    # 发送方法  第一个参数为发件人   第二个参数为收件人列表   第三个参数为邮件转字符串
    smtp.sendmail(useremail,['2606662988@qq.com'],sendtest.as_string())
    # 退出链接
    smtp.quit()
except Exception as e:
    print(e)



