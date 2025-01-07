from flask import Flask
from controllers.user_controller import UserController

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running ..."

if __name__ == "__main__":
    app.run(debug=True)