from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
app = Flask(__name__)


users = {
    "John": generate_password_hash("hello"),
    "Susan": generate_password_hash("bye")
}


@app.route('/')
@auth.login_required
def hello_world():
    return "Hello, %s!" % auth.current_user()


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
