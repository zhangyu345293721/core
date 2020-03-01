# -*- coding:utf-8 -*-
'''
# 测试邮件发送
author:zhangyu
date:2020/2/29
'''

from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = '345293721@qq.com'
app.config['MAIL_PASSWORD'] = 'enulibfvtbuibhed'  # 授权码

mail = Mail(app)

from flask_mail import Message

msg = Message(
    subject="Hello World!",
    body="test...",
    sender="345293721@qq.com",
    recipients=["18062434115@163.com"]
)


@app.route('/')
def hello_world():
    mail.send(msg)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
