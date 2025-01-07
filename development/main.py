from flask import Flask, request
from controllers.user_controller import UserController

app = Flask(__name__)

@app.get("/")
def login():
    return UserController.render_login()

@app.route("/login/process", methods=['POST'])
def process_login():
    return UserController.process_login()

if __name__ == "__main__":
    app.run(debug=True)