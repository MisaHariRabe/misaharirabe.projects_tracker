from flask import Flask
from models.user_model import UserModel

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is on"

if __name__ == "__main__":
    app.run(debug=True)