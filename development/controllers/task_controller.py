from flask import render_template, url_for, redirect, session, flash
from utils.auth_utils import login_required
from models.task_model import TaskModel
from models.project_model import ProjectModel
from forms.project_forms import TaskForm


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
        form = TaskForm()
        return render_template("tasks/create_task.html", form=form, project_id=project_id)
    
    @staticmethod
    @login_required
    def process_create_task(project_id):
        form = TaskForm()
        if not form.validate_on_submit():
            return render_template("tasks/create_task.html", form=form, project_id=project_id)

        try:
            project = ProjectModel.get_by_project_id(project_id)
            if not project or project[5] != session["user_id"]:
                flash("Project not found", "error")
                return redirect(url_for("render_projects"))

            TaskModel.create(
                task_name=form.task_name.data,
                task_description=form.task_description.data,
                project_id=project_id
            )
            flash("Task created successfully", "success")
            return redirect(f"/tasks/{project_id}")
        except Exception as e:
            flash("An error occured while creating the task", "error")
            return render_template("tasks/create_task.html", form=form, project_id=project_id)
    
    @staticmethod
    @login_required
    def process_update_state(project_id, task_id):
        try:
            TaskModel.update_state_by_task_id(task_id)
        except Exception as e:
            flash("An error occured while updating the task", "error")
        finally:
            return redirect(f"/tasks/{project_id}")
        
    @staticmethod
    @login_required
    def process_delete_task(project_id, task_id):
        try:
            TaskModel.delete_by_task_id(task_id)
        except Exception as e:
            flash("An error occured while deleting the task", "error")
        finally:
            return redirect(f"/tasks/{project_id}")