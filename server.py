from flask import Flask, flash, redirect, url_for, request, get_flashed_messages, render_template, send_from_directory
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
import os, requests
from werkzeug import secure_filename

<<<<<<< HEAD
def createInstance():
    options = ['a', 'b', 'c', 'd']
    for option in options:
        if not os.path.isfile(option + '.txt'):
            createTextFile(option)
    
def createTextFile(name):
    file = open(name + '.txt', 'w')
    file.close()

def answerQuestion(answer):
    if answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd':
        file = open(answer + '.txt', 'a')
        file.write(answer)
        file.close()
    else:
        print("Invalid Answer")
    
def sendAnswers():
    options = ['a', 'b', 'c', 'd']
    for option in options:
        sendAnswer(option)

def sendAnswer(answer):
    file = open(answer + '.txt', 'r')
    url = '0.0.0.0'
    requests.post(url, data = '')
    print(len(file.readline()))
    file.close()

=======
>>>>>>> origin/master
app = Flask(__name__, static_folder='static', static_url_path='')


#Start Server at Port 5000
if os.getenv("VCAP_APP_PORT"):
    port = int(os.getenv("VCAP_APP_PORT"))
else:
    port = 80

# use for encrypt session
app.config['SECRET_KEY'] = 'b56936b292f44fc397f77d882b3418ee'




login_manager = LoginManager()
login_manager.init_app(app)

class UserNotFoundError(Exception):
    pass
class User(UserMixin):
    '''Simple User class'''
    USERS = {
        # user : 
        'Jessie Pullaro': '2345'
    }

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        '''Return user instance of id, return None if not exist'''
        try:
            return self_class(id)
        except UserNotFoundError:
            return None

# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.get(id)

@app.route('/')
def index():
    if current_user.is_authenticated:
        user= user=current_user.get_id()
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/dashboard', methods = ['POST', 'GET'])
def dash():
<<<<<<< HEAD
    if request.method == 'POST':
        createInstance()
=======
>>>>>>> origin/master
    if current_user.is_authenticated:
        user = user=current_user.get_id()
        return render_template('dashboard.html',user=user or 'Guest')
    else:
        return redirect('/')

@app.route('/login/student')
def student_login():
    if current_user.is_authenticated:
        user = user=current_user.get_id()
        return redirect('/dashboard')
    else:
        return render_template('student_login.html')

@app.route('/teach_dashboard')
def teach_dashboard():
    if current_user.is_authenticated:
        user = user=current_user.get_id()
        return render_template('teach_dashboard.html')
    else:
        return redirect('/')


@app.route('/login/check', methods=['post'])
def login_check():
    # validate username and password
    user = User.get(request.form['username'])
    if (user and user.password == request.form['password']):
        login_user(user)
    else:
        flash('Username or password incorrect')

    return redirect(url_for('dash'))

@app.route('/logout')
def logout():
    logout_user()
    if current_user.is_authenticated:
        user = user=current_user.get_id()
        return redirect('/dashboard')
    else:
        return render_template('student_login.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug = True)
