#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_email.py
@Author: gentle.yu
@Date  : 2020/8/4 17:34
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ------------1、设置发现相关参数----------
smtpserver = "smtp.sina.com"  # 发件服务器
port = 25  # 端口
sender = "yuyanchao0627@sina.com"  # 账号
psw = "YU80230627aini%"  # 密码
receiver = "1406243734@qq.com"  # 接受人

# -----------2、编辑邮件内容-------------

# 读文件
# file_path = "case_email.py"
# with open(file_path, "rb") as fp:
#     mail_body = fp.read()

msg = MIMEMultipart()
msg['from'] = sender    # 发件人
msg['to'] = receiver    # 接收人
subject = "这个是主题sina邮箱"
msg['subject'] = subject    # 主题

# 正文
text = '<p>这是一封测试邮件</p>'  # 定义邮件正文为html格式
# msg = MIMEText(body, "html", "utf-8")
body = MIMEText(text, "html", "utf-8")
msg.attach(body)

# 附件
att = MIMEText(text, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="case_email.py"'
msg.attach(att)


# ------------3、发送邮件---------------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  # 链接服务器
    smtp.login(sender, psw)  # 登录
except: # 兼容sina邮箱和qq邮箱
    smtp = smtplib.SMTP.SSL(smtpserver, port)
    smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()  # 关闭
