from flask import Flask
from flask import request,render_template
import logging; logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
   

@app.route('/signin', methods=['GET'])
def signin_form():
    
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)