from flask import render_template, request, redirect, session
from utils.auth_utils import login_required
from models.task_model import TaskModel
from models.project_model import ProjectModel


class TaskController:
    @staticmethod
    @login_required
    def render_tasks_list(project_id):
        project = ProjectModel.get_by_project_id(project_id)
        tasks = TaskModel.get_by_project_id(project_id)
        return render_template("tasks/tasks.html", project=project, tasks=tasks)

    @staticmethod
    @login_required
    def render_create_task(project_id):
        return render_template("tasks/create_task.html", project_id=project_id)
    
    @staticmethod
    @login_required
    def process_create_task(project_id):
        data = request.form
        task_name = data.get("task_name")
        task_description = data.get("task_description")
        TaskModel.create(task_name, task_description, project_id)
        return redirect(f"/tasks/{project_id}")
    
    @staticmethod
    @login_required
    def process_update_state(project_id, task_id):
        try:
            TaskModel.update_state_by_task_id(task_id)
        except:
            print("Error: There was an error when you tried to update the task")
        finally:
            return redirect(f"/tasks/{project_id}")
        
    @staticmethod
    @login_required
    def process_delete_task(project_id, task_id):
        try:
            TaskModel.delete_by_task_id(task_id)
        except:
            print("Error: There was an error when you tried to delete the task")
        finally:
            return redirect(f"/tasks/{project_id}")