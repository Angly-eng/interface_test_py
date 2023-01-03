# -*- coding = utf-8 -*-
from flask import Flask, request, render_template, redirect, session,url_for
app = Flask(__name__)
app.debug = True
app.secret_key = "sadfasdfasdf"
USERS = {
 1:{'name':'张三','age':18,'gender':'男','text':'道路千万条'},
 2:{'name':'李四','age':28,'gender':'男','text':'安全第⼀条'},
 3:{'name':'王五','age':18,'gender':'⼥','text':'⾏⻋不规范'},
}
@app.route('/detail/<int:nid>',methods=['GET'])
def detail(nid):
 user = session.get('user_info')
 if not user:
    return redirect('/login')
 info = USERS.get(nid)
 return render_template('detail.html',info=info)

@app.route('/index',methods=["GET"])
def index():
 user = session.get('user_info')
 if not user:
    url = url_for('l1')
    return redirect(url)
 return render_template('index.html',user_dict=USERS)
@app.route('/login',methods=['GET','POST'],endpoint='l1')
def login():
 if request.method == "GET":
    return render_template("login.html")
 else:
    user = request.form.get("user")
    pwd = request.form.get('pwd')
 if user == 'admin' and pwd =='123':
    session['user_info'] = user
    return redirect('/index')
 return render_template('login.html',error="⽤户名密码错误")

if __name__ == '__main__':
    app.run()
