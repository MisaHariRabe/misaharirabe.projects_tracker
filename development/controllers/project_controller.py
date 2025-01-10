from models.project_model import ProjectModel
from flask import render_template, redirect, request, url_for, session
from utils.auth_utils import login_required

class ProjectController:
    @staticmethod
    @login_required
    def render_create_project_form():
        return render_template("projects/create_project.html")

    @staticmethod
    @login_required
    def render_projects_list():
        user_id = session["user_id"]
        projects = ProjectModel.get_by_user_id(user_id)
        return render_template("projects/projects.html", projects=projects)
    
    @staticmethod
    @login_required
    def process_create_project():
        user_id = session["user_id"]
        data = request.form
        project_name = data.get("project_name")
        project_description = data.get("project_description")
        ProjectModel.create(project_name, project_description, user_id)
        return redirect(url_for("render_projects"))
    
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