# -*- coding = utf-8 -*-
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


# 伪登录程序
@app.route('/api/login/', methods=['post'])
def login():
    # 登录成功返回信息
    succmsg = {
        'token': 'zxcdc',
        'msg': '登录成功'
    }
    # 登录失败返回信息
    failmsg = {
        'msg': '登录失败'
    }
    print(request.headers)
    txt = request.get_json()
    print(txt)
    user = txt['username']
    pwd = txt['password']
    # print(user, pwd)
    if user == 'admin' and pwd == '123456':
        res = make_response(jsonify(succmsg))
        return res
    return make_response(jsonify(failmsg))

# 获取客户信息
@app.route('/api/getuserinfo/', methods=['get'])
def getuserinfo():
    # 请求头{"token":  all_values['var_token']}
    print(request.headers)
    _succmsg = {
        'nickname': "风清扬",
        'openid': 1
    }
    _failmsg={
        'msg': 'token验证未通过'
    }
    for i in request.headers:
        if i[0] == 'Token' and i[1] == 'zxcdc':
            print(i)
            print(type(i))
            # 验证信息通过，返回客户信息
            res = make_response(jsonify(_succmsg), 200)
            return res
    else:
        # 验证信息不通过
        return make_response(jsonify(_failmsg),400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
