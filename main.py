from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

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
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()