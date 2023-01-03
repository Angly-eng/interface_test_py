# -*- coding = utf-8 -*-
import requests
# 成功调佣登陆接口，msg返回success
def login():
    url1 = 'http://localhost:5000/api/login/'
    _header = {
        "Content-Type":"application/json"
    }
    _data = {
        "username": "admin","password": "123456"
    }
    a = requests.post(url1, params=_header, json=_data)
    print(a.headers)
    print(a.json())
    global token
    token = a.json()['token']

# 成功调用用户查询接口，nikename返回风清扬
def getusrinfo(token):
    url2 = 'http://localhost:5000/api/getuserinfo/'
    _head ={
        "token": token
    }
    a = requests.get(url=url2, headers=_head)
    print(a.status_code)
    print(a.json())

if __name__ == '__main__':
    token = ''
    login()
    print(token)
    getusrinfo(token)


