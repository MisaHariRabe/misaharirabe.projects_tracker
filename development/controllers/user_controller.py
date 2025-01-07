from models.user_model import UserModel
from flask import render_template, redirect, url_for, request

class UserController:
    @staticmethod
    def render_signup():
        return render_template("users/signup.html")
    
    @staticmethod
    def render_login():
        return render_template("users/login.html")