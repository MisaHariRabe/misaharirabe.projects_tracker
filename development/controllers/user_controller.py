from models.user_model import UserModel
from flask import render_template, redirect, url_for, request, session, flash
from utils.auth_utils import login_required
from forms.auth_forms import LoginForm, SignupForm

class UserController:
    @staticmethod
    def render_signup():
        form = SignupForm()
        return render_template("users/signup.html", form=form)
    
    @staticmethod
    def render_login():
        form = LoginForm()
        return render_template("users/login.html", form=form)
    
    @staticmethod
    def process_signup():
        form = SignupForm()
        if not form.validate_on_submit():
            return render_template("users/signup.html", form=form)

        if UserModel.get_by_email(form.user_email.data):
            flash("Un compte existe déjà avec cet email", "error")
            redirect(url_for("signup"))
        
        try:
            UserModel.create(
                form.user_name.data,
                form.user_dateofbirth.data,
                form.user_email.data,
                form.user_password.data
            )
            flash("Compte créé avec succès", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash("Une erreur s'est produite lors de la création du compte", "error")
            return render_template("users/signup.html", form=form)
    
    @staticmethod
    def process_login():
        form = LoginForm()
        if not form.validate_on_submit():
            return render_template("users/login.html", form=form)

        user = UserModel.get_by_email(form.user_email.data)
        if not user or not UserModel.verify_password(form.user_password.data, user[4]):
            flash("Email ou mot de passe incorrect", "error")
            return render_template("users/login.html", form=form)
        
        session["user_id"] = user[0]
        return redirect("/projects")
    
    @staticmethod
    @login_required
    def process_logout():
        session.pop("user_id")
        return redirect(url_for("login"))