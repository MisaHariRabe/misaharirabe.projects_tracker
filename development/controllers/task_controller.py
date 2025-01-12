from flask import render_template, url_for, redirect, session, flash
from utils.auth_utils import login_required
from models import db
from models.task_model import Task
from models.project_model import Project
from forms.project_forms import TaskForm


class TaskController:
    @staticmethod
    @login_required
    def render_tasks_list(project_id):
        project = Project.query.filter(Project.project_id==project_id).one()
        tasks = Task.query.filter(Task.project_id == project_id).all()
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
            project = Project.query.filter(Project.project_id == project_id).one_or_none()
            if not project or project.user_id != session["user_id"]:
                flash("Project not found", "error")
                return redirect(url_for("render_projects"))

            Task.create(
                task_name=form.task_name.data,
                task_description=form.task_description.data,
                project_id=project_id
            )
            flash("Task created successfully", "success")
            return redirect(f"/tasks/{project_id}")
        except Exception as e:
            flash("An error occured while creating the task", "error")
            print(e)
            return render_template("tasks/create_task.html", form=form, project_id=project_id)
    
    @staticmethod
    @login_required
    def process_update_state(project_id, task_id):
        try:
            task = Task.query.get_or_404(task_id)
            user_id = Project.query.get_or_404(project_id).user_id
            if user_id != session["user_id"]:
                flash("Forbidden Access", "error")
                return redirect(url_for("render_projects"))
            
            task.task_state = True
            db.session.commit()
            flash("Task updated successfully", "success")
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("An error occured while updating the task", "error")
        finally:
            return redirect(f"/tasks/{project_id}")
        
    @staticmethod
    @login_required
    def process_delete_task(project_id, task_id):
        try:
            task = Task.query.get_or_404(task_id)
            user_id = Project.query.get_or_404(project_id).user_id
            if user_id != session["user_id"]:
                flash("Forbidden Access", "error")
                return redirect(url_for("render_tasks"))
            
            db.session.delete(task)
            db.session.commit()
            flash("Task deleted successfully", "success")
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("An error occured while deleting the task", "error")
        finally:
            return redirect(f"/tasks/{project_id}")