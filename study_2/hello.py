# Flask类的实例是WSGI 应用程序WSGI是Web Server Gateway Interface的缩写。

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    pass
    
@app.route('/login')
def login():
    pass

@app.route('/projects/<username>')
def hello_world(username):
    pass

# with app.test_request_context():
#     print url_for('index')
#     print url_for('login')
#     print url_for('login', next='/')
#     print url_for('profile', username='John Doe')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
