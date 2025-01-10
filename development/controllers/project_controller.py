from models.project_model import ProjectModel
from flask import render_template, redirect, url_for, session, flash
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
        projects = ProjectModel.get_by_user_id(user_id)
        return render_template("projects/projects.html", projects=projects)
    
    @staticmethod
    @login_required
    def process_create_project():
        form = ProjectForm()
        if not form.validate_on_submit():
            return render_template("projects/create_project.html", form=form)

        try:
            user_id = session["user_id"]
            ProjectModel.create(
                form.project_name.data,
                form.project_description.data,
                user_id
            )
            flash("Projet créé avec succès", "success")
            return redirect(url_for("render_projects"))
        except Exception as e:
            flash("Une erreur s'est produite lors de la création du projet", "error")
            return render_template("projects/create_project.html", form=form)
    
    
    @staticmethod
    @login_required
    def process_update_state(project_id):
        try:
            ProjectModel.update_state_by_project_id(project_id)
        except:
            print("Error: There was an error when you tried to update the project")
        finally:
            return redirect(url_for("render_projects"))
    
    @staticmethod
    @login_required
    def process_delete_project(project_id):
        try:
            ProjectModel.delete_by_project_id(project_id)
        except:
            print("Error: There was an error when you tried to delete the project")
        finally:
            return redirect(url_for("render_projects"))