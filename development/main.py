from flask import Flask, request
from controllers.user_controller import UserController

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return UserController.render_login()
    elif request.method == 'POST':
        return UserController.process_login()

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return UserController.render_signup()
    elif request.method == 'POST':
        return UserController.process_signup()


if __name__ == "__main__":
    app.run(debug=True)