from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'routes list: yoboi, notyoboi, /user/<username>'

@app.route('/yoboi')
def yoboi():
    return 'its ya boi'
    
@app.route('/notyoboi')
def notyoboi():
    return 'its not ya boi'

@app.route('/user/<username>')
def your_profile(username):
    return 'Welcome %s' %username