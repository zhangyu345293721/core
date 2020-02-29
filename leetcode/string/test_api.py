# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/27
'''
from flask import Flask, request

app = Flask(__name__)

'''
@app.route('/add', methods=['GET'])
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    result = int(a) + int(b)
    return str(result)
'''


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) + int(b)
    return str(result)


@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'


# 对外提供服务
if __name__ == '__main__':
    app.run(debug=True)
