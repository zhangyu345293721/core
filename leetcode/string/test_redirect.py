from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest')
def hello_guest():
    guest = request.args.get('guest')
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


from flask import request


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file_name']
        f.save('d://zhang.jpg')
        # 把流存入到数据库

    return '1'


if __name__ == '__main__':
    app.run(debug=True)
