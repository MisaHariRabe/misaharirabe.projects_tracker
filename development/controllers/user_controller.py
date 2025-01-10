from models.user_model import UserModel
from flask import render_template, redirect, url_for, request, session, flash
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

        existing_user = UserModel.get_by_email(user_email)
        if existing_user:
            flash("Un compte existe déjà avec cet email", "error")
            redirect(url_for("signup"))
        
        try:
            UserModel.create(user_name, user_dateofbirth, user_email, user_password)
            flash("Compte créé avec succès", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash("Une erreur s'est produite lors de la création du compte", "error")
            return redirect(url_for("signup"))
    
    @staticmethod
    def process_login():
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        user = UserModel.get_by_email(user_email)

        if not user:
            flash("Email incorrect", "error")
            return redirect(url_for("login"))
        
        if not UserModel.verify_password(user_password, user[4]):
            flash("Mot de passe incorrect", "error")
            return redirect(url_for("login"))
        
        session["user_id"] = user[0]
        return redirect("/projects")
    
    @staticmethod
    @login_required
    def process_logout():
        session.pop("user_id")
        return redirect(url_for("login"))