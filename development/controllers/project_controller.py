from models.project_model import ProjectModel
from flask import render_template, redirect, request, session, url_for
from utils.auth_utils import AuthUtils

class ProjectController:
    @staticmethod
    def render_create_project_form():
        AuthUtils.isAuthenticated()
        return render_template("projects/create_project.html")

    @staticmethod
    def render_projects_list():
        user_id = AuthUtils.isAuthenticated()
        projects = ProjectModel.get_by_user_id(user_id)
        return render_template("projects/projects.html", projects=projects)
    
    @staticmethod
    def process_create_project():
        user_id = AuthUtils.isAuthenticated()
        data = request.form
        project_name = data.get("project_name")
        project_description = data.get("project_description")
        ProjectModel.create(project_name, project_description, user_id)
        return redirect(url_for("render_projects"))
    
    @staticmethod
    def process_update_state(project_id):
        AuthUtils.isAuthenticated()
        try:
            ProjectModel.update_state_by_project_id(project_id)
        except:
            print("Error: There was an error when you tried to update the project")
        finally:
            return redirect(url_for("render_projects"))
    
    @staticmethod
    def process_delete_project(project_id):
        try:
            ProjectModel.delete_by_project_id(project_id)
        except:
            print("Error: There was an error when you tried to delete the project")
        finally:
            return redirect(url_for("render_projects"))