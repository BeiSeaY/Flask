from flask import Flask
from flask import request,make_response,redirect,abort
from flask_script import Manager


app = Flask(__name__) #flask 类的构造函数只有一个必须制定的参数，
# 即程序都主模块或包都名字，在大多数程序中，python都name变量就是所需的值

# @app.route('/')#修饰器。把修饰器函数注册为路由，使用这个修饰器声明路由
# def inder():
#     return '<h1> Hello Word </h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1> hello ,%s </h1>' % name

# @app.route('/user/agent')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your brower is {}</p>'.format(user_agent)

# print(app.url_map) # URL映射和URL视图的对应关系

# @app.route('/')
# def index():
#     return '<h1>自定义状态码默认200</h1>',400

# @app.route('/')
# def index():
#     respones = make_response('<h1>make_response()函数可接受1,2,3个参数，并返回一response对象</h1>') # 和视图函数返回值一样
#     respones.set_cookie('answer','42')
#     return respones

# @app.route('/')
# def index():
#     return redirect('https://cn.bing.com/') # 重定向辅助函数，302状态码，一个页面没有文档，告诉浏览器加载新的页面

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404) # 特殊响应函数，用来处理错误，如果URL中动态参数不对，就返回错误状态码
          #abort不会把控制权交给调用他的函数，而是抛出异常把控制权交给Web服务器
#     return '<h1>hello, %s</h1>'%user.name

manager = Manager(app) # flask扩展

@app.route('/')
def index():
    return redirect('http://www.baidu.com')

if __name__ == "__main__":
    manager.run() #python hello.py runserver --help

# if __name__ == "__main__": # 启动服务
#     app.run(debug=True)
