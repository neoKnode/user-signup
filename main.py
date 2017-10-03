<<<<<<< HEAD
from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
=======
from flask import Flask
>>>>>>> e3e5161551bcaf7f4c097214cba84bfd07aab76f

app = Flask(__name__)
app.config['DEBUG'] = True

<<<<<<< HEAD
@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/welcome", methods=['POST'])
def welcome():
    first_name = request.form['userfield']
    template = jinja_env.get_template('welcome.html')
    return template.args.get(name=userfield)
=======
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 1px;
            }

        </style>
    </head>
    <body>
         <form method="POST">
            <label for="username">Username</label>
            <input id="username" type="text" name="userfield" value="" />
            <br>
            <br>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form
>>>>>>> e3e5161551bcaf7f4c097214cba84bfd07aab76f

app.run()