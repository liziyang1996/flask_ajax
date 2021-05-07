import random

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('user.html')


@app.route('/random')
def gennm():
    maxnum = request.args.get('max')
    value = random.randint(0, int(maxnum))
    return str(value)

@app.route('/check', methods=['get', 'post'])
def checkUser():
    usernames = ['zhangsan', 'lisi', 'wangwu']
    username = request.form.get('username')
    res = {'flag':0} # 用户不存在 可以注册
    if username in usernames:
        res['flag'] = 1

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)