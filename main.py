# -*- coding = utf-8 -*-
import os
import pytest

if __name__ == '__main__':

    # pytest写测试用例
    # pytest.main(['-s', '--alluredir','./result','--clean-alluredir'])
    # os.system("allure serve result")

    # excel写测试用例
    # excel文件地址
    path = r'D:\shanchu\interface_demo\excel_read\testcase_file\test_exce_main.py'
    pytest.main(['-vs', '--alluredir' ,'./result', '--clean-alluredir', path])
    # os.system("allure serve result")
    os.system("allure generate ./result -o ./report --clean")



#
# class LogicGate:
#
#     def __init__(self, n):
#         self.label = n
#         self.output = None
#
#     def getlabel(self):
#         return self.label
#
#     def performGateLogic(self):
#         pass
#
#     def getOutput(self):
#         self.output = self.performGateLogic()
#         return self.output
#
#
#
#
# class BinaryGate(LogicGate):
#
#     def __init__(self, n):
#         super().__init__(n)
#
#         self.pinA = None
#         self.pinB = None
#
#     def getPinA(self):
#         if self.pinA == None:
#             return int(input(f"请输入{self.getlabel()}号A引脚"))
#         else:
#             return self.pinA
#     def getPinB(self):
#         if self.pinB == None:
#             return int(input(f"请输入{self.getlabel()}号B引脚"))
#         else:
#             return self.pinB
#
#     def setNextPin(self, sourse):
#         if self.pinA == None:
#             self.pinA = sourse
#         else:
#             if self.pinB == None:
#                 self.pinB = sourse
#             else:
#                 raise RuntimeError("PIN已被占用")
#
# class UnaryGate(LogicGate):
#
#     def __init__(self, n):
#         super().__init__(n)
#
#         self.pin = None
#
#     def getPin(self):
#         if self.pin is None:
#             return int(input(f"请输入{{非门}}{self.getlabel()}号引脚"))
#         else:
#             return self.pin
#
#     def setNextPin(self, sourse):
#         if self.pin == None:
#             self.pin = sourse
#         else:
#             raise RuntimeError("PIN已被占用")
# class Connector():
#
#     def __init__(self, fgate, tgate):
#         self.fromgate = fgate
#         self.togate = tgate
#         print(f"正在创建{fgate}{fgate.getlabel()}和{tgate}{tgate.getlabel()}的连接")
#         a = fgate.getOutput()
#         tgate.setNextPin(a)      #将上一逻辑门结果存入PIN
#     def getFrom(self):
#         return self.fromgate
#
#     def getTo(self):
#         return self.togate
#
# class AndGate(BinaryGate):
#
#     def __init__(self, n):
#         super().__init__(n)
#
#     def __str__(self):
#         return "   {与门}  "
#
#     def performGateLogic(self):
#         a = self.getPinA()
#         b = self.getPinB()
#         if a == 1 and b == 1:
#             return 1
#         else:
#             return 0
#
# class OrGate(BinaryGate):
#
#     def __init__(self, n):
#         super().__init__(n)
#
#     def __str__(self):
#         return "   {或门}  "
#
#     def performGateLogic(self):
#         a = self.getPinA()
#         b = self.getPinB()
#         if a == 1 or b == 1:
#             return 1
#         else:
#             return 0
#
# class NotGate(UnaryGate):
#
#     def __init__(self, n):
#         super().__init__(n)
#
#     def __str__(self):
#         return "   {非门}  "
#
#     def performGateLogic(self):
#         a = self.getPin()
#         return 1 - a
#
# g1 = AndGate("1")
# g2 = NotGate("2")
# g3 = OrGate("3")
# c1 = Connector(g1, g3)
# # print("pinA为", g3.pinA)
# c2 = Connector(g2, g3)
# # print("pinB", g3.pinB)
# print(g3.getOutput())

# def func_1(s1, s2):
#     if s1 == s2:
#         return False
#     c1 = {}
#     c2 = {}
#     for i in s1:
#         if c1.get(i) is not None:
#             c1[i] = c1[i] + 1
#         else:
#             c1[i] = 1
#
#     for i in s2:
#         if c2.get(i) is not None:
#             c2[i] = c2[i] + 1
#         else:
#             c2[i] = 1
#
#     if c1 == c2:
#         return True
#     else:
#         print(c1,c2)
#         return False
#
#
#
# print(func_1('ABCD','BCBBEA'))

# from flask import Flask, request, render_template, redirect, session,url_for
# app = Flask(__name__)
# app.debug = True
# app.secret_key = "sadfasdfasdf"
# USERS = {
#  1:{'name':'张三','age':18,'gender':'男','text':'道路千万条'},
#  2:{'name':'李四','age':28,'gender':'男','text':'安全第⼀条'},
#  3:{'name':'王五','age':18,'gender':'⼥','text':'⾏⻋不规范'},
# }
# @app.route('/detail/<int:nid>',methods=['GET'])
# def detail(nid):
#  user = session.get('user_info')
#  if not user:
#     return redirect('/login')
#  info = USERS.get(nid)
#  return render_template('detail.html',info=info)
#
# @app.route('/index',methods=["GET"])
# def index():
#  user = session.get('user_info')
#  if not user:
#     url = url_for('l1')
#     return redirect(url)
#  return render_template('index.html',user_dict=USERS)
# @app.route('/login',methods=['GET','POST'],endpoint='l1')
# def login():
#  if request.method == "GET":
#     return render_template("login.html")
#  else:
#     user = request.form.get("user")
#     pwd = request.form.get('pwd')
#  if user == 'admin' and pwd =='123':
#     session['user_info'] = user
#     return redirect('/index')
#  return render_template('login.html',error="⽤户名密码错误")
#
# if __name__ == '__main__':
#     app.run()

# def b():
#     num2=1
#     def c():
#         nonlocal num2#为了修改非全局变量
#         num2+=2
#         print(num2)
#     return c
# b()()
# print(b())


