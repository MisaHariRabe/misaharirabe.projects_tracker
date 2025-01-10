from flask import render_template, redirect, url_for, session, flash
from models import db
from models.project_model import Project
from utils.auth_utils import login_required
from forms.project_forms import ProjectForm

class ProjectController:
    @staticmethod
    @login_required
    def render_create_project_form():
        form = ProjectForm()
        return render_template("projects/create_project.html", form=form)

    @staticmethod
    @login_required
    def render_projects_list():
        user_id = session["user_id"]
        projects = Project.query.filter_by(user_id=user_id).all()
        return render_template("projects/projects.html", projects=projects)
    
    @staticmethod
    @login_required
    def process_create_project():
        form = ProjectForm()
        if not form.validate_on_submit():
            return render_template("projects/create_project.html", form=form)

        try:
            user_id = session["user_id"]
            Project.create(
                project_name=form.project_name.data,
                project_description=form.project_description.data,
                user_id=user_id
            )
            flash("Project created successfully", "success")
            return redirect(url_for("render_projects"))
        except Exception as e:
            flash("An error occured while creating the project", "error")
            return render_template("projects/create_project.html", form=form)
    
    
    @staticmethod
    @login_required
    def process_update_state(project_id):
        try:
            project = Project.query.get_or_404(project_id)
            if project.user_id != session["user_id"]:
                flash("Forbidden Access", "error")
                return redirect(url_for("render_projects"))
            
            project.project_state = True
            db.session.commit()
            flash("Project updated successfully", "success")
        except Exception as e:
            db.session.rollback()
            flash("An error occured while updating the project", "error")
        return redirect(url_for("render_projects"))
    
    @staticmethod
    @login_required
    def process_delete_project(project_id):
        try:
            project = Project.query.get_or_404(project_id)
            if project.user_id != session["user_id"]:
                flash("Forbidden Access", "error")
                return redirect(url_for("render_projects"))
            
            db.session.delete(project)
            db.session.commit()
            flash("Project deleted successfully", "success")
        except Exception as e:
            db.session.rollback()
            flash("An error occured while updating the project", "error")
        return redirect(url_for("render_projects"))