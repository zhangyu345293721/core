# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/29
'''
from io import BytesIO

from PIL import Image
from flask import Flask, redirect, url_for, make_response
from flask import request

from leetcode.flask_demo.database_orm import get_algo_model, save_algo_model

app = Flask(__name__)


def converse_bytes_2_picture(algo: bytes) -> None:
    '''
        将bytes转化为图片
    Args:
        algo:比特流
    '''
    # 将bytes结果转化为字节流
    bytes_stream = BytesIO(algo)
    roiimg = Image.open(bytes_stream)
    roiimg.show()


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest')
def hello_guest():
    guest = request.args.get('guest')
    return 'Hello %s as Guest' % guest


# 测试重定向
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# get请求
@app.route('/add1', methods=['GET'])
def add1():
    a = request.args["a"]
    b = request.args["b"]
    result = int(a) + int(b)
    return str(result)


# 测试post请求
@app.route('/add2', methods=['POST'])
def add2():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) + int(b)
    return str(result)


# 上传图片到服务器（数据库）
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file_name']
        name = request.form['name']
        img = f.read()
        # 把流存入到数据库
        save_algo_model(name, img)
    return 'success'


# 客户端从数据库下载图片,然后网页上显示
@app.route('/download', methods=['GET'])
def down_file():
    name = request.args.get('name')
    img = get_algo_model(name)
    response = make_response(img)
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == '__main__':
    app.run(debug=True)
