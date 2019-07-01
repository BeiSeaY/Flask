
from flask import Flask
from flask import request

app = Flask(__name__) #flask 类的构造函数只有一个必须制定都参数，
# 即程序都主模块或包都名字，在大多数程序中，python都name变量就是所需的值

@app.route('/')#修饰器。把修饰器函数注册为路由，使用这个修饰器声明路由
def inder():
    return '<h1> Hello Word </h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1> hello ,%s </h1>' % name

@app.route('/user/agent')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brower is {}</p>'.format(user_agent)

if __name__ == "__main__": #启动服务
    app.run(debug=True)