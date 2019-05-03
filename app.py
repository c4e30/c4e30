from flask import Flask, render_template, request, redirect, url_for, session
from db import find_username, add_user, get_all
app = Flask(__name__)
app.secret_key = 'abjhejkwiooo123123'

@app.route('/signup')
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods= ["POST"])
def post_signup():
    username = request.form.get('username')
    password = request.form.get('password')
    nick_name = request.form.get('nick_name')
    if find_username(username) == None:
        add_user(username,nick_name,password)
        return render_template('index.html')
    else:
        return redirect(url_for('get_signup'))

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/', methods = ["POST"])
def post_index():
    username = request.form.get('username')
    password = request.form.get('password')
    user = {
        'username':username,
        'password':password
    }
    if user in get_all():
        session['username'] = username
        return 'đã đăng nhập thành công'
    return redirect(url_for('get_index'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 