from models.user_model import UserModel
from flask import render_template, redirect, url_for, request, session
from utils.auth_utils import login_required

class UserController:
    @staticmethod
    def render_signup():
        return render_template("users/signup.html")
    
    @staticmethod
    def render_login():
        return render_template("users/login.html")
    
    @staticmethod
    def process_signup():
        user_name = request.form["user_name"]
        user_dateofbirth = request.form["user_dateofbirth"]
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        UserModel.create(user_name, user_dateofbirth, user_email, user_password)
        return redirect(url_for("login"))
    
    @staticmethod
    def process_login():
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        user = UserModel.get_by_email(user_email)
        if not user:
            return redirect("/")
        if user[4] != user_password:
            return redirect(url_for("login"))
        session["user_id"] = user[0]
        return redirect("/projects")
    
    @staticmethod
    @login_required
    def process_logout():
        session.pop("user_id")
        return redirect(url_for("login"))