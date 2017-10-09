
from flask import Flask, request, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('signup_form.html')


@app.route('/', methods=['POST'])
def validate_user():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Username too short/long'


    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Password too short/long'

    if verify_password == '':
        verify_error = 'Please retype your password'

    if password != verify_password:
        verify_error = 'Passwords do not match!'

    if email != '' and len(email) < 3 or len(email) > 20:
        email_error = 'Email too short/long'
    
    elif email != '' and ("@" not in email) or ("." not in email) or (' ' in email):
        email_error = 'Please enter a valid email'

    elif email.count("@") != 1 or email.count(".") != 1:
        email_error = 'Please enter a valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template('signup_form.html', username=username,
            email=email, username_error=username_error, 
            password_error=password_error, verify_error=verify_error, 
            email_error=email_error)

app.run()